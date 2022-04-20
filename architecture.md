---
layout: page
title: VocaLiST
subtitle: An Audio-Visual Synchronisation Model for Lips and Voices
---

<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
    VocaLiST (acronym for <strong>Voca</strong>l <strong>Li</strong>p <strong>S</strong>ynchronisation <strong>T</strong>ransformer),
    is a novel audio-visual transformer-based lip-voice synchronisation model 
    that estimates the extent of synchronisation between the lips motion 
    and the voice in a given voice video. Fig. 1 shows the high-level
    architecture of the entire model.
</div>

<div class="center" style="text-align: center">
    <div class="center col-md-5" style="text-align: center">
        <img src="../img/high_level.png"/>
    </div>
    <span>Fig 1. High level architecture of our lip synchronisation model.</span>
</div>

<!--<div style="display: flex">
    <div class="col-md-6" style="text-align: center">
        <img src="../img/all_arch.png" style="height: 75%;max-width:105%"/>
        <span>Fig 1. Architecture of our lip synchronisation model.</span>
    </div>
    <div class="col-md-6" style="text-align: center;">
        <img src="../img/audio_visual_encoder.png" style="height: 75%; width: 96%;"/>
        <span>Fig 2. Our audio encoder (left) and visual encoder (right).</span>
    </div>
</div>-->

<!--<h4 style="margin-top:-4em;">Audio Encoder</h4>-->
<br>
<h4>Audio Encoder</h4>
<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
Our audio encoder is very similar to the audio encoder used in
the lip-sync expert discriminator [1]. The architecture details
are shown in Fig. 2 (left). The audio encoder is a stack of 2D 
convolutional layers with residual skip-connections that operate on
the mel-spectrogram input of dimensions 1 × 80 × t<sub>a</sub> . The
mel-spectrograms are obtained using 80 mel-filterbanks with a
hop size of 200 and window size of 800. The audios have a
16kHz sampling rate. The audio features are of the dimension
512 × t<sub>a</sub>. The audio encoder conserves the temporal 
resolution of the input.</div>
<div class="center" style="text-align: center">
    <div class="center col-md-8" style="text-align: center">
        <img src="../img/audio_visual_encoder.png"/>
    </div>
    <span>Fig 2. Our audio encoder (left) and visual encoder (right).</span>
</div>


<br>
<h4>Visual Encoder</h4>
<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
The visual encoder ingests a sequence of RGB images cropped
around the mouth having dimensions 3×48×96×t<sub>v</sub>. Its 
architecture is inspired by the visual encoder of the lip-sync expert
discriminator. Unlike in the latter, we apply 3D convolutions
and conserve the temporal resolution in the feature maps. The
output visual features are of dimension 512 × t<sub>v</sub> . The conservation
of temporal resolution in both the audio and visual features
is helpful for learning the synchronisation patterns between the
two modalities spread across the temporal dimension when we
feed them into the synchronisation module. The visual frames
are sampled from videos of 25 fps.</div>
<br>
<h4>Synchronisation Block</h4>
<div class="lead mb-0" align="justify">
<p>We design a powerful cross-modal audio-visual transformer that
can use the audio-visual representations learned in its cross-modal 
attention modules to deduce the inherent audio-visual
correspondence in a synchronised voice and lips motion pair.
We refer to our transformer model as VocaLiST, the Vocal Lip
Sync Transformer. Its design is inspired by the cross-modal
transformer from [2]. The cross-modal attention blocks track
correlations between signals across modalities.</p>
</div>
<div class="center" style="text-align: center">
    <div class="center col-md-5" style="text-align: center">
        <img src="../img/sync_block.png"/>
    </div>
    <span>Fig 3. Architecture of Synchronisation block of VocaLiST</span>
</div>
<br>
<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
<p>The synchronisation block contains three cross-modal
transformer encoders, each made up of 4 layers, 8 attention
heads and the hidden unit dimension of 512. The A→V unit
takes in audio features as the query and the visual features as the
key and values. The roles of these audio and visual features is
swapped in the V→A unit. The output of the A→V unit forms
the query to the hybrid fusion transformer unit, while its key
and values are sourced from the output of the V→A unit. We
max-pool the output of this hybrid fusion unit along the temporal
dimension and pass it through tanh activation. Fig. 1 shows
the architecture of VocaLiST.</p>

<p>Finally, there is a fully-connected layer acting as a classifier
which outputs a score indicating if the voice and lips motion are
synchronised or not. The whole architecture can handle any
length of audio and visual inputs.</p></div>

<div class="row">
    <h3 class="col-sm-4" style="display: inline-block">References</h3>
</div>

<p class="lead mb-0" align="justify">

    [1] K. Prajwal, R. Mukhopadhyay, V. P. Namboodiri, and C. Jawahar,
    “A lip sync expert is all you need for speech to lip generation in the
    wild,” in Proceedings of the 28th ACM International Conference  
    on Multimedia, 2020, pp. 484–492.
    <br>
    [2] Y.-H. H. Tsai, S. Bai, P. P. Liang, J. Z. Kolter, L.-P. Morency, and
    R. Salakhutdinov, “Multimodal transformer for unaligned multimodal 
    language sequences,” in Proceedings of the conference.
    Association for Computational Linguistics. Meeting, vol. 2019.
    NIH Public Access, 2019, p. 6558.
</p>

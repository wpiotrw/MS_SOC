---
layout: Conceptual
title: Graphics encoding over Direct Stream - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/graphics-encoding
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: agacadsioson
manager: eliotgra
ms.author: agacadsioson
ms.service: azure-virtual-desktop
description: Learn how graphics data, including text, images, and video, is encoded and delivered over Direct Stream. It applies to Azure Virtual Desktop, Windows 365, and Microsoft Dev Box.
ms.topic: how-to
ms.date: 2024-10-15T00:00:00.0000000Z
locale: en-us
document_id: b896637c-1445-2dbb-25fe-aa790f327d86
document_version_independent_id: b896637c-1445-2dbb-25fe-aa790f327d86
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/graphics-encoding.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: graphics-encoding
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/graphics-encoding.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: 0e5ad139-bb34-08af-057c-18057ba5d4cf
---

# Graphics encoding over Direct Stream - Azure Virtual Desktop | Microsoft Learn

Graphics data from a remote session is transmitted to a local device via Direct Stream (DS). The process involves encoding the graphics data on the remote virtual machine before sending it to the local device. Each frame is processed based on its content, passing through image processors, a classifier, and a codec, before being delivered to the local device using DS's graphics transport.

The aim of encoding and transmitting graphics data is to provide optimal performance and quality, with an experience that is the same as using a device locally. This process is important when using Azure Virtual Desktop, Cloud PCs in Windows 365, and Microsoft Dev Box, where users expect a high-quality experience when working remotely.

DS uses a range of features and techniques to process and transmit graphics data that make it suitable for a wide range of scenarios, such as office productivity, video production, design, and video playback. These features and techniques include:

- **Hardware and software-based encoding**: uses the CPU or GPU to encode graphics data.

    - **Hardware-accelerated encoding**: offloads the processing of graphics encoding from the CPU to the GPU on a remote virtual machine equipped with a capabable GPU. A GPU provides better performance for graphics-intensive applications, such as 3D modeling or high-definition video editing. Compatible GPUs also include specialized video encoding engines which DS can leverage to encode session content.
    - **Software encoding**: uses the CPU to encode graphics data at a low cost. Software encoding is the default encoding profile used on a remote virtual machine without a discrete GPU.
- **Mixed-mode**: separates text, image and video encoding using different codecs to provide the best quality and lowest encoding cost for each type of detected content. Mixed-mode is only available with software encoding.
- **Adaptive graphics**: adjusts the encoding quality based on the available bandwidth and the content of the screen.
- **Full-screen video encoding**: provides a higher frame rate and better user experience in scenarios with high image/video content.
- **Delta detection and caching**: reduces the amount of data that needs to be transmitted.
- **Multiple codec support**: uses hardware decoders on a local device. Codecs include the Advanced Video Coding (AVC) video codec, also known as H.264, and the High Efficiency Video Coding (HEVC) video codec, also known as H.265. HEVC/H.265 support requires a compatible GPU-enabled remote virtual machine.
- **4:2:0 and 4:4:4 chroma subsampling**: provides a balance between image quality and bandwidth usage.

You can use a combination of these features and techniques depending on the available resources of the remote session, local device, and network to deliver the user experience you want to provide.

This article describes the process of encoding and delivering graphics data over DS using some of these features and techniques.

Tip

We recommend you use multimedia redirection where possible, which redirects video playback to the local device. Multimedia redirection provides a better user experience for video playback by sending the bitstream of video data to the local device where it decodes and renders the video in the correct place on the screen. This method also lowers processing cost on the remote virtual machine regardless of encoding configuration. To learn more, see [Multimedia redirection for video playback and calls in a remote session](multimedia-redirection-video-playback-calls).

## Mixed-mode

By default, graphics data is separated depending on its content. Text, images, and videos are encoded using a mix of codecs to achieve optimal encoding performance across different content types when using software encoding only. This process is known as mixed-mode.

On average, approximately 80% of the graphics data for a remote session is text. In order to provide the lowest encoding cost and best quality for text, DS uses a custom codec that's optimized for text. Due to image content being more challenging to encode effectively, it's critical to use a codec that adapts well to available bitrate.

The rest of the content is separated to images and video:

- Images are software encoded with either AVC/H.264 or RemoteFX graphics, depending on the capabilities of the local device. The default encoding of detected image content uses AVC/H.264 when supported by the session endpoint configuration.
- Video is software encoded with AVC/H.264.

AVC/H.264 is a widely supported codec that has good compression ratio for images, is capable of progressive encoding, and has ability to adjust quality based on bitrate. It relies on the hardware decoder on the local device, which is widely supported on modern devices. Using the hardware decoder on the local device reduces the CPU usage on the local device and provides a better user experience. Check with the device manufacturer to ensure that it supports AVC/H.264 hardware decoding.

The following diagram shows the process of encoding and delivering graphics data over DS using mixed-mode in a software encoding scenario:

[![A diagram showing the process of encoding and delivering graphics data over RDP using mixed-mode.](media/graphics-encoding/graphics-encoding-mixed-mode.svg)](media/graphics-encoding/graphics-encoding-mixed-mode.svg#lightbox)

This process is described as follows:

1. A frame bitmap is first processed by detecting whether it contains video. If it does contain video, the frame is sent to the video codec, which in a software-based scenario is encoded with AVC/H.264, and then the frame passes to the graphics channel.
2. If the frame doesn't contain video, the image processors determine if there are delta changes, motion is detected, or if content is available in the cache. If the content matches certain criteria, the frame passes to the graphics channel.
3. If the frame needs further processing, the image classifier determines whether it contains text or images.
4. Text and images are encoded using different codecs to provide the best quality and lowest encoding cost for each type of content. Once encoded, the frame passes to the graphics channel.

Instead of using two separate codecs for text and images with mixed-mode, you can enable full-screen video encoding to process all screen content using the AVC/H.264 video codec.

## Full-screen video encoding

Full-screen video encoding is useful for scenarios where the screen content is largely image based and is used as an alternative to mixed-mode. Full-screen video encoding processes all graphics data with either AVC/H.264 or HEVC/H.265. As a result, it performs worse than mixed-mode encoding when the screen content is largely text based.

A full-screen video profile provides a higher frame rate and better user experience, but uses more network bandwidth and resources on both the remote virtual machine and local device. It benefits applications such as 3D modeling, CAD/CAM, or video playback and editing.

If you enable both HEVC/H.265 and AVC/H.264 hardware acceleration, but HEVC/H.265 isn't available on the local device, AVC/H.264 is used instead. HEVC/H.265 allows for 25-50% data compression compared to AVC/H.264, at the same video quality, or improved quality, at the same bitrate.

You can enable full-screen video encoding with AVC/H.264 even without GPU acceleration, but HEVC/H.265 requires a compatible GPU-enabled remote virtual machine.

To learn more, see [Enable GPU acceleration for Azure Virtual Desktop](enable-gpu-acceleration).

## Hardware GPU acceleration

Azure Virtual Desktop, Cloud PCs in Windows 365, and Microsoft Dev Box support graphics processing unit (GPU) acceleration in rendering and encoding for improved app performance and scalability using Direct Stream (DS). GPU acceleration is crucial for graphics-intensive applications, such as those used by graphic designers, video editors, 3D modelers, data analysts, or visualization specialists.

There are two components to GPU acceleration that work together to improve the user experience:

- **GPU-accelerated application rendering**: Use the GPU to render graphics in a remote session.
- **GPU-accelerated frame encoding**: DS encodes all graphics rendered for transmission to the local device. When part of the screen is frequently updated, it's encoded with AVC/H.264.

If the screen content in your workloads is largely image based, you can also enable full-screen video encoding to process all screen content to provide a higher frame rate and better user experience.

To learn more, see [Enable GPU acceleration](enable-gpu-acceleration).

## Chroma subsampling support for 4:2:0 and 4:4:4

The chroma value determines the color space used for encoding. By default, the chroma value is set to 4:2:0, which provides a good balance between image quality and network bandwidth. To improve image quality, you can increase the chroma value to 4:4:4 by enabling AVC/H.264 full screen encoding and setting Image Quality to High via group policy. You don't need to use GPU acceleration to change the chroma value, however a 4:4:4 chroma value will use more bandwidth for the same frames using 4:2:0.

To learn more, see [Increase the chroma value to 4:4:4 using the Advanced Video Coding (AVC) video codec](graphics-chroma-value-increase-4-4-4).
<h1 align="center"> Image Transformer Program </h1>

<h2 align="center"> Compression </h4>

<h4 align="center"> This feature uses linear algebra to compress an image by a given factor value </h4>
<h4 align="center"> Ex. factor = x means the image will be compressed to take up only 1/x of the original's unique pixel storage </h4>
<h4 align="center"> Note that there is diminishing returns due to the file maintaining the same resolution and that pixel count != local file storage </h4>

<details>
<summary> Image Examples </summary>
<p align="center">
<img width="400" height="300" src="/images/og_image.png">
</p>

<br/>

<p align="center">
<img width="400" height="300" src="/images/imagef2.png">
</p>

<br/>

<p align="center">
<img width="400" height="300" src="/images/imagef4.png">
</p>

<br/>

<p align="center">
<img width="400" height="300" src="/images/imagef8.png">
</p>

<br/>

<p align="center">
<img width="400" height="300" src="/images/imagef16.png">
</p>

<br/>

<p align="center">
<img width="400" height="300" src="/images/imagef50.png">
</p>
</details>

<h2 align="center"> Rotation Feature </h4>

<h4 align="center"> This feature rotates an image clockwise and produces a new image </h4>
<h4 align="center"> Ex. input of 1 means 1 clockwise rotate </h4>

<details>
  <summary> Visual Showcase </summary>
  <p align="center">
  <img width="400" height="300" src="/images/rotation_showcase.gif">
  </p>
</details>

<h2 align="center"> Future Plans </h4>
<details>
  <summary> Click to expand </summary>

  - A main file/function to conduct the messy inputs
  
  - PyInstaller Exectuable File with GUI
  
  - Drag and drop file instead of inputting file name
  
  - Check for valid file
  
  - Potentially allow for rectangular rotation

  - Counter-clockwise rotate to increase 3-rotate efficiency and allow for increased user control

  - Recolor images (gray-scale, reshading, etc)

  - Tangential Ideas (PDF converter)
</details>

#@ String output_file

newImage("Test Image", "8-bit ramp", 256, 256, 1);
run("Statistical Region Merging", "q=25 showaverages");
saveAs("Tiff", output_file);
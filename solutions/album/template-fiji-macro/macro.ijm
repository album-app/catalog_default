#@ String output_file

run("Boats");
run("Statistical Region Merging", "q=25 showaverages");
saveAs("Tiff", output_file);
const font = new FontFace("Aptos", "url(Aptos.ttf)");
document.fonts.add(font);

const bold_font = new FontFace("Aptos-Bold", "url(Aptos-Bold.ttf)");
document.fonts.add(bold_font);

document.fonts.ready.then(() => {
    // All fonts are loaded and ready for use
    console.log("All document fonts are ready.");
    document.body.style.fontFamily ="Aptos";
});
import Image from "@11ty/eleventy-img";

export default function(eleventyConfig) {
	eleventyConfig.addShortcode("image", async function(src, alt, sizes = "100vw") {
		// Resolve path relative to project root
		const imagePath = `./public/${src}`;

		let metadata = await Image(imagePath, {
			widths: ["auto", 400, 800],
			formats: ["avif", "webp", "auto"],
			outputDir: "./_site/img/",
			urlPath: "/img/",
		});

		let imageAttributes = {
			alt,
			sizes,
			loading: "lazy",
			decoding: "async",
		};

		return Image.generateHTML(metadata, imageAttributes);
	});
}

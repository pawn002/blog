import Image from "@11ty/eleventy-img";

export default function (eleventyConfig) {
	// Shortcode for animated GIFs - serves directly without processing
	eleventyConfig.addShortcode("gif", function (src, alt) {
		if (!alt) {
			throw new Error(`Missing alt text for GIF: ${src}`);
		}
		const urlPath = src.startsWith("/") ? src : `/img/${src}`;
		return `<img src="${urlPath}" alt="${alt}" loading="lazy" decoding="async" eleventy:ignore>`;
	});

	eleventyConfig.addShortcode(
		"image",
		async function (src, alt, sizes = "100vw") {
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
		},
	);
}

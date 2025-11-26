# The Compliance Trap: How WCAG's Codification Has Stalled Accessibility Innovation

*An Essay on Regulatory Ossification and the Promise of APCA*

---

Digital accessibility should be a moving target, constantly refined by advances in vision science, display technology, and our understanding of human perception. Instead, the accessibility landscape in private industry has calcified around a standard that even its own governing body acknowledges is deeply flawed. The Web Content Accessibility Guidelines (WCAG), specifically its contrast algorithm, has become so entrenched in legal frameworks that organizations face genuine risk when attempting to adopt superior alternatives—even when those alternatives demonstrably serve disabled users better.

This is the paradox of accessibility compliance in 2025: the very mechanisms intended to protect people with disabilities have become barriers to protecting them more effectively. The Accessible Perceptual Contrast Algorithm (APCA), developed by Andrew Somers and slated for inclusion in WCAG 3.0, represents a significant leap forward in color contrast evaluation. Yet cautious corporate counsel across industries advise against its adoption, not because it fails to serve users, but because WCAG 2.x has been effectively codified as law.

## The Fundamental Flaws of WCAG 2.x Contrast

The problems with WCAG 2.x's contrast algorithm are not matters of minor technical disagreement—they represent fundamental failures in how the standard models human perception. As documented extensively in the W3C's own issue tracking, the contrast ratio math used in WCAG 2.0 and 2.1 is not perceptually uniform, meaning the "contrast ratios" it produces do not correspond meaningfully to how humans actually perceive luminance differences on modern displays. Research conducted by Andrew Somers and independently verified by a PhD researcher at the University of Cambridge found that approximately 47 percent of color combinations that pass WCAG 2.x criteria should actually be rejected due to poor readability. Paradoxically, about 23 percent of colors that WCAG 2.x rejects as non-compliant are, in fact, perfectly readable and in some cases even more suitable for individuals with color vision deficiencies.

The most visible manifestation of this dysfunction is the "orange button problem" that has plagued designers for years. White text on a medium orange background is clearly readable to most users, including many with visual impairments, yet fails WCAG 2.x's 3:1 ratio requirement for large text. Conversely, text with a 4.5:1 ratio against a near-black background can be functionally unreadable, yet passes the standard. As Somers has noted, "WCAG 2 contrast only works when the background is very light or white, and the text is much darker. That's really the only time it works." This limitation renders the current guidelines essentially useless for dark mode interfaces—a design pattern that has become ubiquitous across operating systems and applications.

The consequences are staggering. According to WebAIM's analysis, 86 percent of website home pages fail WCAG 2.x contrast requirements. Some of these failures represent genuinely inaccessible design choices. But as the APCA documentation notes, "some failures are not due to actually poor accessibility, but due to the incorrect math of WCAG 2 contrast." The standard has created a situation where automated testing tools flag accessible color combinations as failures while permitting truly problematic ones, leading to widespread designer frustration and, ultimately, a disregard for contrast guidelines altogether.

## APCA: A Perceptually Accurate Alternative

The Accessible Perceptual Contrast Algorithm addresses these deficiencies by grounding its calculations in modern vision science rather than simplified mathematical ratios. Unlike WCAG 2.x, which treats foreground and background colors symmetrically, APCA recognizes that human contrast perception is polarity-sensitive—swapping text and background colors produces different perceptual results. APCA also accounts for font size and weight, acknowledging that smaller, thinner text requires higher contrast than large, bold headings. This granularity allows designers greater flexibility while actually improving readability outcomes.

APCA reports contrast as a Lightness Contrast (Lc) value ranging from 0 to approximately 106. Unlike WCAG's simple pass/fail thresholds, APCA provides graduated guidance: Lc 15 represents the point of invisibility for many users, Lc 75 is the minimum for body text, and Lc 90 is preferred for optimal readability. This nuanced approach reflects the reality that contrast needs vary based on context, content type, and user characteristics. The algorithm has undergone extensive peer review, including independent studies published in academic journals and evaluations by design professionals across the industry. Peer reviews published by researchers at the Oslo School of Architecture and Design, the University of Cambridge, and numerous industry practitioners have validated APCA's superiority in predicting real-world readability.

Critically, when properly implemented with appropriate font sizes, APCA conformance actually exceeds WCAG 2.x AAA requirements—the highest level of the current standard. This means organizations adopting APCA are not reducing accessibility; they are enhancing it. Yet the path to adoption remains fraught with legal uncertainty.

## The Legal Codification of WCAG

The accessibility regulatory landscape in the United States has effectively transformed WCAG from voluntary guidelines into legal requirements through multiple channels. Section 508 of the Rehabilitation Act, which governs federal agencies and their contractors, explicitly incorporates WCAG 2.0 Level AA by reference. The revised Section 508 standards, published in January 2017, harmonized requirements with WCAG and apply to all federal information and communication technology. Non-compliance can result in formal complaints, civil lawsuits, and administrative penalties.

While the Americans with Disabilities Act (ADA) does not explicitly reference WCAG, Department of Justice enforcement has consistently cited conformance with WCAG 2.1 Level AA as the settlement requirement in accessibility cases. A 2023 report from the U.S. Chamber of Commerce Institute for Legal Reform stated that "three decades after its enactment, much ADA litigation has nothing to do with accessibility, but rather has become characterized by abusive lawsuits run by a small group of lawyers and law firms." According to data compiled by UsableNet and other researchers, ADA digital accessibility lawsuits have increased substantially since 2013, with annual filings consistently exceeding 4,000 cases in recent years.

This litigation environment creates a perverse incentive structure. Organizations are motivated not to achieve the best possible accessibility outcomes, but to satisfy the specific technical criteria that courts and regulators recognize. When WCAG is the de facto legal standard, deviating from it—even in favor of demonstrably superior alternatives—exposes organizations to risk. As one accessibility consultant has observed, "If you need to be backwards compatible, the new Bridge-PCA can help!" The very existence of a "Bridge PCA" tool designed to provide WCAG 2.x compatibility while using APCA technology speaks to the bind in which organizations find themselves.

## The Compliance Culture Problem

The entrenchment of WCAG as a legal standard has given rise to what might be termed a "compliance culture" in corporate accessibility—an orientation toward checking boxes rather than serving users. Organizations often treat accessibility as a technical checkbox exercise rather than an opportunity to create genuinely inclusive experiences. This mindset manifests in reactive, audit-driven approaches focused on avoiding litigation rather than proactive investment in inclusive design.

The business case for minimal compliance typically centers on risk avoidance and legal obligation, focusing on avoiding lawsuits and fines as the primary motivator. This stands in stark contrast to organizations that view accessibility as a driver of innovation, brand differentiation, and market expansion. The W3C's Web Accessibility Initiative has documented how accessibility improvements often drive broader innovation and remove barriers that affect all users. Yet when legal risk dominates decision-making, innovation becomes an afterthought.

This dynamic is particularly frustrating because accessibility improvements often benefit all users, not just those with disabilities. Voice control interfaces, originally developed for users who cannot use traditional inputs, have become mainstream conveniences. Curb cuts designed for wheelchair users are appreciated by parents with strollers, travelers with luggage, and delivery workers with carts. When compliance culture constrains accessibility thinking, these broader innovations suffer.

## The Path Forward

WCAG 3.0, which will incorporate APCA, remains years away from becoming an official W3C Recommendation. According to Andrew Somers, the algorithm's creator, "it's going to be at least another four years, I think, until WCAG 3 is the actual recommendation." In the interim, organizations face a difficult choice: adhere to a standard they know to be flawed, or adopt superior approaches that may expose them to legal uncertainty.

Some practitioners advocate a dual approach—measuring against both WCAG 2.x and APCA simultaneously, meeting the legal requirement while also achieving better accessibility outcomes. As one accessibility professional has advised: "Measure in WCAG but also measure in APCA, so that you have met that legal requirement there with the colors—or conformance rather." This approach is workable but adds complexity and cost to design and development workflows.

A more fundamental solution would require regulatory evolution. If Section 508 were updated to reference WCAG 3.0 or to explicitly permit conformance with APCA as an alternative standard, organizations would have clearer latitude to adopt improved methods. Similarly, DOJ guidance acknowledging APCA as an acceptable approach to ADA compliance would significantly reduce legal risk. Such changes would align legal frameworks with the actual goal of accessibility law: ensuring that people with disabilities can perceive, navigate, and interact with digital content.

## Conclusion

The current state of accessibility compliance represents a failure of the regulatory feedback loop. Standards that were adequate for CRT displays and core web fonts in 2008 have been frozen in place by legal codification, preventing the natural evolution that technical standards require. Meanwhile, display technology has advanced dramatically, design patterns like dark mode have become standard, and vision science has provided much deeper understanding of human perception.

The disability community deserves better than a contrast algorithm that approves unreadable color combinations while rejecting accessible ones. They deserve guidelines built on perceptual accuracy rather than mathematical convenience. They deserve an accessibility framework that can evolve as technology and science advance.

Until regulatory bodies catch up with accessibility science, the compliance trap will persist. Organizations will continue to optimize for legal defensibility rather than user experience. Designers will continue to wrestle with guidelines that often produce worse outcomes than their trained instincts would suggest. And the vision of truly inclusive digital experiences will remain constrained by standards that, ironically, were intended to advance it.

The solution is not to abandon compliance—legal protections for accessibility are essential and hard-won. The solution is to ensure that what we are complying with actually serves the people these protections exist to help. APCA offers that possibility. The question is whether our legal and regulatory structures can evolve quickly enough to embrace it.

---

## Sources

1. Myndex Research. "Why APCA as a New Contrast Method?" APCA Documentation. https://git.apcacontrast.com/documentation/WhyAPCA.html

2. W3C. "Contrast Ratio Math and Related Visual Issues." GitHub Issue #192, WCAG 3.0 Repository. https://github.com/w3c/wcag3/issues/192

3. Gratzer, Colleen. "How APCA Changes Accessible Contrast — With Andrew Somers." Medium, December 2023. https://medium.com/@colleengratzer/how-apca-changes-accessible-contrast-with-andrew-somers-3d47627a5e16

4. Bureau of Internet Accessibility. "86 Percent of Websites Fail this Accessibility Basic." May 2021. https://www.boia.org/blog/86-percent-of-websites-fail-this-accessibility-basic

5. U.S. Access Board. "IT Accessibility Laws and Policies." Section508.gov. https://www.section508.gov/manage/laws-and-policies/

6. Level Access. "ADA vs. 508 compliance vs. WCAG: Your source of truth." https://www.levelaccess.com/blog/ada-vs-section-508-whats-the-difference/

7. W3C. "Contrast Research: APCA Peer Reviews + Defining a Visual Contrast Guideline." GitHub Issue #29, WCAG 3.0 Repository. https://github.com/w3c/wcag3/issues/29

8. Shopify. "The small business shakedown: Why thousands of entrepreneurs are getting buried in lawsuits." https://www.shopify.com/news/accessibility-lawsuits

9. W3C. "The Business Case for Digital Accessibility." Web Accessibility Initiative. https://www.w3.org/WAI/business-case/

10. Eggert, Eric. "WCAG 3 is not ready yet – And it won't be for quite some time." https://yatil.net/blog/wcag-3-is-not-ready-yet

11. University of Bath. "The times they are a-changin' (for how we measure colour contrast)." Digital Content and Development Blog, November 2024. https://blogs.bath.ac.uk/digital-content-and-development/2024/11/08/the-times-they-are-a-changin-for-how-we-measure-colour-contrast/

12. UsableNet. "ADA Website Compliance Lawsuit Tracker." https://info.usablenet.com/ada-website-compliance-lawsuit-tracker

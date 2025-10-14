import { exec } from "child_process";
import { promises as fs } from "fs";
import path from "path";

// Configuration
const SOURCE_REPO = "C:\\Users\\pawn0\\_dev\\blog"; // Local path or URL of the source repo
const TARGET_REPO = "C:\\Users\\pawn0\\_dev\\blog-public"; // Local path or URL of the target repo
const TARGET_BRANCH = "prod";
const DOCS_FOLDER = "docs";

// Function to run shell commands
const runCommand = (command) => {
	return new Promise((resolve, reject) => {
		exec(`powershell.exe -Command "${command}"`, (error, stdout, stderr) => {
			if (error) {
				reject(new Error(`Command failed: ${command}\nError: ${stderr}`));
			} else {
				resolve(stdout);
			}
		});
	});
};

// Function to check if a directory exists
const dirExists = async (dirPath) => {
	try {
		await fs.access(dirPath);
		return true;
	} catch {
		return false;
	}
};

const publish = async () => {
	try {
		// Check if the source repo exists
		if (!(await dirExists(SOURCE_REPO))) {
			throw new Error(`Source repository not found: ${SOURCE_REPO}`);
		}

		// Check if the target repo exists
		if (!(await dirExists(TARGET_REPO))) {
			throw new Error(`Target repository not found: ${TARGET_REPO}`);
		}

		// Navigate to target repo and checkout the prod branch
		await runCommand(
			`Set-Location -Path "${TARGET_REPO}"; git checkout ${TARGET_BRANCH}; git pull`
		);

		// Check if the docs folder exists in the source repo
		const sourceDocsPath = path.join(SOURCE_REPO, DOCS_FOLDER);
		if (!(await dirExists(sourceDocsPath))) {
			throw new Error(
				`Docs folder not found in source repo: ${sourceDocsPath}`
			);
		}

		// Clear existing docs in target repo
		const targetDocsPath = path.join(TARGET_REPO, DOCS_FOLDER);
		if (await dirExists(targetDocsPath)) {
			await runCommand(
				`Remove-Item -Path "${targetDocsPath}\*" -Recurse -Force`
			);
		}

		// Copy new docs
		await runCommand(
			`Copy-Item -Path "${sourceDocsPath}\*" -Destination "${targetDocsPath}" -Recurse`
		);

		// Stage, commit, and push changes
		await runCommand(`Set-Location -Path "${TARGET_REPO}"; git add .`);
		await runCommand(
			`Set-Location -Path "${TARGET_REPO}"; git commit -m "Update docs"`
		);

		// Push to the branch
		await runCommand(
			`Set-Location -Path "${TARGET_REPO}"; git push origin ${TARGET_BRANCH}`
		);

		console.log("Docs published successfully!");
	} catch (error) {
		console.error(
			"An error occurred during the publish process:",
			error.message
		);
	}
};

publish();

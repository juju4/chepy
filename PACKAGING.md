# Packaging CI/CD

Binary file is generated with pyinstaller and packaged and/or signed.
Signature is either codesign keyless mode, either self-signed certificate that should be replaced by whatever certificate authority is applicable to your context (public or private).

## Linux

* Sign with codesign in keyless mode
* deb/rpm?

## Macos

* Sign with codesign in keyless mode
* package, codesign?

## Windows

* makeappx, signtool
* pymsix
* wixtoolset?

Signing

* [Active Directory Certificate Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/)
* [Azure Artifact Signing](https://azure.microsoft.com/en-us/products/artifact-signing)
  * [Artifact Signing trust models](https://learn.microsoft.com/en-us/azure/artifact-signing/concept-trust-models): Public, Private (with AppControl/WDAC)

## Extras

* SBOM?
* files Hash listing?
* Clamav scan?
  * <https://github.com/toblux/start-clamd-github-action>

## Resources

* [winapp - CLI Documentation and Usage](https://learn.microsoft.com/en-us/windows/apps/dev-tools/winapp-cli/usage)
* [Configure CI/CD pipeline with YAML file](https://learn.microsoft.com/en-us/windows/msix/desktop/azure-dev-ops)
* [How to create a basic package manifest for Windows 8](https://learn.microsoft.com/en-us/uwp/schemas/appxpackage/how-to-create-a-basic-package-manifest)
* [CI/CD pipeline to Sign and Notarize Electron Apps, Sep 2022](https://www.codiga.io/blog/notarize-sign-electron-app/)
* [Packaging and publishing Intune apps using Winget and Azure Devops CI/CD Pipeline – packaging as code, Nov 2022](https://andrewstaylor.com/2022/11/15/packaging-and-publishing-intune-apps-using-winget-and-azure-devops-ci-cd-pipeline-packaging-as-code/), <https://github.com/andrew-s-taylor/public/blob/main/Powershell%20Scripts/Intune/add-winget-package-pipeline.ps1>
* [How to upload the build on microsoft intune through azure devops pipelines, Feb 2025](https://stackoverflow.com/questions/79436088/how-to-upload-the-build-on-microsoft-intune-through-azure-devops-pipelines), <https://gist.github.com/Hesamedin/cde8eee8abd0c44e007925c75a2a0b99>

* [Automatic Code-signing and Notarization for macOS apps using GitHub Actions, Aug 2022](https://federicoterzi.com/blog/automatic-code-signing-and-notarization-for-macos-apps-using-github-actions/)
* [Distributing Mac Apps With GitHub Actions, Sep 2023](https://defn.io/2023/09/22/distributing-mac-apps-with-github-actions/)
* [CI-Ready macOS Signing: Combining Apple Distribution & Installer Certificates for GitHub Actions, Mar 2025](https://msicc.net/ci-ready-macos-signing-combining-certs-for-github-actions/)
* [Signing and Notarizing with GitHub Actions](https://gregoryszorc.com/docs/apple-codesign/stable/apple_codesign_github_actions.html)
* [Automating packaging and software distribution on macOS.](https://github.com/autopkg/autopkg)

* [Effing package management! Build packages for multiple platforms (deb, rpm, etc) with great ease and sanity.](https://github.com/jordansissel/fpm) (ruby)
* Fedora [Packaging Tutorial 1: banner](https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_1_banner/)

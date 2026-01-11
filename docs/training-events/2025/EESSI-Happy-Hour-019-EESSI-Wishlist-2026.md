# Notes for EESSI Happy Hour #19 (22 December 2025)

*Topic: EESSI-Christmas: Whishlist for 2026*

- new EESSI version, scheduled before summer
    - yearly cycle for EESSI versions
    - using 2026 or 2026a compiler toolchain
- how long will we add software to EESSI 2023.06?
    - no clear policy on this yet, task for EESSI Steering Committee
    - how many active EESSI versions at a time?
    - when is an EESSI version archived?
- software overview
    - [see mockup](https://users.ugent.be/~kehoste/EFP/mockup-software-overview-20251113/software-cards-dynamic-local-links.html)
- EESSI CLI as improved user interface
    - beyond modules
- license checking
    - make it required for EESSI 2026.X
- improvements to the bot
    - tarball analysis to make ingestion easier
    - overview of differences between tarballs
- support for AMD GPUs (ROCm)
    - should look into [https://github.com/ROCm/TheRock](https://github.com/ROCm/TheRock)
    - limited demand currently, only LUMI (+ upcoming Alice Recoque)
    - [https://github.com/vosen/ZLUDA](https://github.com/vosen/ZLUDA)
    - via ROCm project in `dev.eessi.io`
    - ongoing work in EasyBuild
        - strange problem with ROCm-LLVM in jsc-zen3 bot is still unresolved
- `dev.eessi.io`
    - policy on lifetime for installations
- new CPU targets
    - AMD Turin (Zen5)
    - Graviton 3+4
    - only for EESSI 2025.06 + upcoming EESSI versions
- list of software that's work-in-progress or in high demand?
    - anonymous requests?
    - could be powered by Google Forms, triggers PR to docs
    - incl. overview of WIP PRs in software-layer repo
- documented roadmap for EESSI for coming year
    - should be done early next year

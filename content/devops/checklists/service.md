---
title: "Service"
draft: false
description: "Comprehensive DevOps checklist for launching a new service, covering version control, CI/CD, networking, observability, databases, and security."
summary: "A step-by-step checklist to ensure your new service is production-ready, from initial setup to monitoring and rollback strategies."
---

## New service

- [ ] Version control system
    - [ ] Workflow
    - [ ] Semantic versioning
- [ ] CI/CD
    - [ ] Build
        - [ ] Upload artifacts
    - [ ] Deploy
        - [ ] Configurations
        - [ ] Cetificates
        - [ ] Artifacts
    - [ ] Unit tests
    - [ ] Linters
    - [ ] Quality gates
    - [ ] Rollback
    - [ ] DevSecOps
        - [ ] Pre-commit
            - Local checks
        - [ ] Pre-build
            - Secrets detection
            - Sast
            - Source SCA
        - [ ] Post-build
            - Binary SCA
        - [ ] Test-time
            - DAST
            - IAST
            - OAST
        - [ ] Post-deploy
            - RAST
- [ ] Network shielding
- [ ] Metrics
    - [ ] Version
    - [ ] Build date
- [ ] Obsevability
    - [ ] Collection a metrics
    - [ ] Collection a logs
    - [ ] Collection a trace
- [ ] Forwading/location
- [ ] Database
- [ ] Queue
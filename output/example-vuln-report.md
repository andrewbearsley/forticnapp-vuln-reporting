# FortiCNAPP Host Vulnerability Report

**Generated:** 2026-02-18 16:20
**Minimum severity:** Critical
**Fixable only:** Yes

## Summary

| Metric | Count |
|--------|-------|
| Unique CVEs | 73 |
| Vulnerable packages | 19 |
| Affected hosts | 4 |
| Critical findings | 102 |
| High findings | 0 |

## Top Packages to Remediate (40)

| # | Package | Namespace | Fix Version | CVEs | Hosts | Score |
|---|---------|-----------|-------------|------|-------|-------|
| 1 | minimist | npm | 1.2.6 | CVE-2021-44906 | 3 | 13.38 |
| 2 | form-data | npm | 2.5.4 | CVE-2025-7783 | 2 | 12.96 |
| 3 | elliptic | npm | 6.6.1 | GHSA-vjh7-7g9h-fjfh | 2 | 12.96 |
| 4 | pbkdf2 | npm | 3.1.3 | CVE-2025-6545, CVE-2025-6547 | 2 | 12.96 |
| 5 | minimist | npm | 0.2.4 | CVE-2021-44906 | 2 | 12.8 |
| 6 | growl | npm | 1.10.0 | CVE-2017-16042 | 2 | 12.8 |
| 7 | json-schema | npm | 0.4.0 | CVE-2021-3918 | 2 | 12.8 |
| 8 | lodash | npm | 4.17.12 | CVE-2019-10744 | 2 | 12.1 |
| 9 | sha.js | npm | 2.4.12 | CVE-2025-9288 | 2 | 12.1 |
| 10 | cipher-base | npm | 1.0.5 | CVE-2025-9287 | 2 | 12.1 |
| 11 | form-data | npm | 4.0.4 | CVE-2025-7783 | 1 | 11.96 |
| 12 | Microsoft Windows Server 2022 | win:s2022 | KB5066782 | CVE-2016-9535, CVE-2025-49708 | 1 | 11.9 |
| 13 | deep-extend | npm | 0.5.1 | CVE-2018-3750 | 1 | 11.8 |
| 14 | socket.io-parser | npm | 4.2.1 | CVE-2022-2421 | 1 | 11.8 |
| 15 | fsevents | npm | 1.2.11 | CVE-2023-45311, GHSA-xv2f-5jw4-v95m | 1 | 11.8 |
| 16 | deeply | npm | 3.1.0 | CVE-2019-10750 | 1 | 11.8 |
| 17 | Microsoft Windows Server 2022 | win:s2022 | KB5068787 | CVE-2025-60724 | 1 | 11.8 |
| 18 | Microsoft Windows Server 2022 | win:s2022 | KB5070884 | CVE-2025-59287 | 1 | 11.8 |
| 19 | Microsoft Windows Server 2022 | win:s2022 | KB5063812 | CVE-2025-50177, CVE-2025-53766 | 1 | 11.8 |
| 20 | handlebars | npm | 4.7.7 | CVE-2021-23369, CVE-2021-23383 | 1 | 11.8 |
| 21 | cryptiles | npm | 4.1.2 | CVE-2018-1000620 | 1 | 11.8 |
| 22 | handlebars | npm | 4.3.0 | CVE-2019-19919 | 1 | 11.8 |
| 23 | xmlhttprequest-ssl | npm | 1.6.1 | CVE-2021-31597 | 1 | 11.4 |
| 24 | cryptography | python | 3.3.2 | CVE-2020-36242 | 1 | 11.1 |
| 25 | Microsoft Windows Server 2022 | win:s2022 | KB5058385 | CVE-2025-29966, CVE-2025-29967 | 1 | 10.8 |
| 26 | @babel/traverse | npm | 7.23.2 | CVE-2023-45133 | 1 | 10.8 |
| 27 | Microsoft Windows Server 2022 | win:s2022 | KB5065432 | CVE-2025-53800, CVE-2025-54918 | 1 | 10.8 |
| 28 | Microsoft Windows Server 2022 | win:s2022 | KB5049983 | CVE-2025-21294, CVE-2025-21295, CVE-2025-21296 (+4) | 1 | 10.1 |
| 29 | Microsoft Windows Server 2022 | win:s2022 | KB5055526 | CVE-2025-26663, CVE-2025-26670, CVE-2025-26686 (+3) | 1 | 10.1 |
| 30 | Microsoft Windows Server 2022 | win:s2022 | KB5053603 | CVE-2025-24035, CVE-2025-24045, CVE-2025-24064 (+2) | 1 | 10.1 |
| 31 | Microsoft Windows Server 2022 | win:s2022 | KB5058500 | CVE-2025-29833, CVE-2025-32710 | 1 | 10.1 |
| 32 | xmlhttprequest-ssl | npm | 1.6.2 | CVE-2020-28502 | 1 | 10.1 |
| 33 | Microsoft Windows Server 2022 | win:s2022 | KB5052106 | CVE-2025-21376 | 1 | 10.1 |
| 34 | Microsoft Windows Server 2022 | win:s2022 | KB5060526 | CVE-2025-49735 | 1 | 10.1 |
| 35 | Microsoft Windows Server 2022 | win:s2022 | KB5060525 | CVE-2025-29828, CVE-2025-33070, CVE-2025-33071 | 1 | 10.1 |
| 36 | Microsoft Windows Server 2022 | win:s2022 | KB5065306 | CVE-2025-48807, CVE-2025-53799, CVE-2025-55224 (+3) | 1 | 9.8 |
| 37 | Microsoft Windows Server 2022 | win:s2022 | KB5063880 | CVE-2025-50176, CVE-2025-53778 | 1 | 9.8 |
| 38 | Microsoft Windows Server 2022 | win:s2022 | KB5073457 | CVE-2026-20822 | 1 | 9.8 |
| 39 | Microsoft Windows Server 2022 | win:s2022 | KB5068840 | CVE-2025-60716 | 1 | 9.0 |
| 40 | Microsoft Windows Server 2022 | win:s2022 | KB5062572 | CVE-2024-36350, CVE-2024-36357, CVE-2025-47980 (+2) | 1 | 8.2 |

### 1. minimist (npm)

- **Fix version:** 1.2.6
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2021-44906
- **Affected hosts:** 3

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 1.2.0 | 11.8 |
| ip-172-17-1-165.ap-southeast-1.compute.internal | i-017ae4a71a0aeb374 | 1.2.5 | 11.8 |
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 1.2.5 | 11.8 |

### 2. form-data (npm)

- **Fix version:** 2.5.4
- **Severities:** Critical
- **Max CVSS:** 9.96
- **CVEs:** CVE-2025-7783
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 2.3.1 | 11.96 |
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 2.1.4 | 11.96 |

### 3. elliptic (npm)

- **Fix version:** 6.6.1
- **Severities:** Critical
- **Max CVSS:** 9.96
- **CVEs:** GHSA-vjh7-7g9h-fjfh
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 6.5.2 | 11.96 |
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 6.4.0 | 11.96 |

### 4. pbkdf2 (npm)

- **Fix version:** 3.1.3
- **Severities:** Critical
- **Max CVSS:** 9.96
- **CVEs:** CVE-2025-6545, CVE-2025-6547
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 3.0.12 | 11.96 |
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 3.0.14 | 11.96 |

### 5. minimist (npm)

- **Fix version:** 0.2.4
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2021-44906
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 0.0.10 | 11.8 |
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 0.0.8 | 11.8 |

### 6. growl (npm)

- **Fix version:** 1.10.0
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2017-16042
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 1.9.2 | 11.8 |
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 1.9.2 | 11.8 |

### 7. json-schema (npm)

- **Fix version:** 0.4.0
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2021-3918
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 0.2.3 | 11.8 |
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 0.2.3 | 11.8 |

### 8. lodash (npm)

- **Fix version:** 4.17.12
- **Severities:** Critical
- **Max CVSS:** 9.1
- **CVEs:** CVE-2019-10744
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 4.17.4 | 11.1 |
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 4.17.5 | 11.1 |

### 9. sha.js (npm)

- **Fix version:** 2.4.12
- **Severities:** Critical
- **Max CVSS:** 9.1
- **CVEs:** CVE-2025-9288
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 2.4.10 | 11.1 |
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 2.4.11 | 11.1 |

### 10. cipher-base (npm)

- **Fix version:** 1.0.5
- **Severities:** Critical
- **Max CVSS:** 9.1
- **CVEs:** CVE-2025-9287
- **Affected hosts:** 2

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 1.0.3 | 11.1 |
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 1.0.4 | 11.1 |

### 11. form-data (npm)

- **Fix version:** 4.0.4
- **Severities:** Critical
- **Max CVSS:** 9.96
- **CVEs:** CVE-2025-7783
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 4.0.1 | 11.96 |

### 12. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5066782
- **Severities:** Critical
- **Max CVSS:** 9.9
- **CVEs:** CVE-2016-9535, CVE-2025-49708
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 11.9 |

### 13. deep-extend (npm)

- **Fix version:** 0.5.1
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2018-3750
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 0.4.2 | 11.8 |

### 14. socket.io-parser (npm)

- **Fix version:** 4.2.1
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2022-2421
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 2.3.1 | 11.8 |

### 15. fsevents (npm)

- **Fix version:** 1.2.11
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2023-45311, GHSA-xv2f-5jw4-v95m
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 1.1.1 | 11.8 |

### 16. deeply (npm)

- **Fix version:** 3.1.0
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2019-10750
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 1.0.0 | 11.8 |

### 17. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5068787
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2025-60724
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 11.8 |

### 18. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5070884
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2025-59287
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 11.8 |

### 19. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5063812
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2025-50177, CVE-2025-53766
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 11.8 |

### 20. handlebars (npm)

- **Fix version:** 4.7.7
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2021-23369, CVE-2021-23383
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 4.0.11 | 11.8 |

### 21. cryptiles (npm)

- **Fix version:** 4.1.2
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2018-1000620
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 3.1.2 | 11.8 |

### 22. handlebars (npm)

- **Fix version:** 4.3.0
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2019-19919
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 4.0.11 | 11.8 |

### 23. xmlhttprequest-ssl (npm)

- **Fix version:** 1.6.1
- **Severities:** Critical
- **Max CVSS:** 9.4
- **CVEs:** CVE-2021-31597
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 1.5.3 | 11.4 |

### 24. cryptography (python)

- **Fix version:** 3.3.2
- **Severities:** Critical
- **Max CVSS:** 9.1
- **CVEs:** CVE-2020-36242
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-49.ap-southeast-1.compute.internal | i-0799e3a4b56be2630 | 3.2.1 | 11.1 |

### 25. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5058385
- **Severities:** Critical
- **Max CVSS:** 8.8
- **CVEs:** CVE-2025-29966, CVE-2025-29967
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.8 |

### 26. @babel/traverse (npm)

- **Fix version:** 7.23.2
- **Severities:** Critical
- **Max CVSS:** 8.8
- **CVEs:** CVE-2023-45133
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 7.9.0 | 10.8 |

### 27. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5065432
- **Severities:** Critical
- **Max CVSS:** 8.8
- **CVEs:** CVE-2025-53800, CVE-2025-54918
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.8 |

### 28. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5049983
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2025-21294, CVE-2025-21295, CVE-2025-21296, CVE-2025-21297, CVE-2025-21298, CVE-2025-21307, CVE-2025-21309
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 29. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5055526
- **Severities:** Critical
- **Max CVSS:** 8.1
- **CVEs:** CVE-2025-26663, CVE-2025-26670, CVE-2025-26686, CVE-2025-27480, CVE-2025-27482, CVE-2025-27491
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 30. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5053603
- **Severities:** Critical
- **Max CVSS:** 8.8
- **CVEs:** CVE-2025-24035, CVE-2025-24045, CVE-2025-24064, CVE-2025-24084, CVE-2025-26645
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 31. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5058500
- **Severities:** Critical
- **Max CVSS:** 8.1
- **CVEs:** CVE-2025-29833, CVE-2025-32710
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 32. xmlhttprequest-ssl (npm)

- **Fix version:** 1.6.2
- **Severities:** Critical
- **Max CVSS:** 8.1
- **CVEs:** CVE-2020-28502
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-10-100-3-123.ap-southeast-1.compute.internal | i-0f3c4563f1c12a574 | 1.5.3 | 10.1 |

### 33. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5052106
- **Severities:** Critical
- **Max CVSS:** 8.1
- **CVEs:** CVE-2025-21376
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 34. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5060526
- **Severities:** Critical
- **Max CVSS:** 8.1
- **CVEs:** CVE-2025-49735
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 35. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5060525
- **Severities:** Critical
- **Max CVSS:** 8.1
- **CVEs:** CVE-2025-29828, CVE-2025-33070, CVE-2025-33071
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 10.1 |

### 36. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5065306
- **Severities:** Critical
- **Max CVSS:** 7.8
- **CVEs:** CVE-2025-48807, CVE-2025-53799, CVE-2025-55224, CVE-2025-55226, CVE-2025-55228, CVE-2025-55236
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 9.8 |

### 37. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5063880
- **Severities:** Critical
- **Max CVSS:** 8.8
- **CVEs:** CVE-2025-50176, CVE-2025-53778
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 9.8 |

### 38. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5073457
- **Severities:** Critical
- **Max CVSS:** 7.8
- **CVEs:** CVE-2026-20822
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 9.8 |

### 39. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5068840
- **Severities:** Critical
- **Max CVSS:** 7.0
- **CVEs:** CVE-2025-60716
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 9.0 |

### 40. Microsoft Windows Server 2022 (win:s2022)

- **Fix version:** KB5062572
- **Severities:** Critical
- **Max CVSS:** 9.8
- **CVEs:** CVE-2024-36350, CVE-2024-36357, CVE-2025-47980, CVE-2025-47981, CVE-2025-48822
- **Affected hosts:** 1

| Hostname | Instance | Version | Score |
|----------|----------|---------|-------|
| ip-172-17-2-185.ap-southeast-1.compute.internal | i-0c8104214f010bf57 | KB5048654 | 8.2 |

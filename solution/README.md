### **Step 1: Clone a Shumlow-Ferguson dual_ec_backdoor Proof of Concept GitHub Repo**
- **Folder**: `1_dual_ec_backdoor_poc_repo`
- **Description**: Anton Kueltz' proof of concept provides a simple way to test the Shumlow-Ferguson exploit in Python. Participants will need to search for one of these repos and hard-code the parameters to understand how this cryptographic PRNG scheme works.
![alt text](1_dual_ec_backdoor_poc_repo/images/Anton_Kueltz_Default_Execution.png)
![alt text](1_dual_ec_backdoor_poc_repo/images/dmhacker_Default_Execution.png)
![alt text](2_dual_ec_backdoor_poc_repo_modified/images/Anton_Kueltz_Modded_Execution.png)

### **Step 2: Reverse Engineer Output Using Parameter Knowledge**
- **Folder**: `2_dual_ec_backdoor_poc_repo_modified`
- **Description**: After having understood how a Dual EC PRNG containing the Shumlow-Ferguson backdoor works, participants must reverse engineer the observed 32-byte block output to gain the current internal state of the PRNG.

### **Step 3: Submit Internal State to Server**
- **Folder**: `3_paste_internal_state_in_cmd`
- **Description**: Participants must quickly paste the internal state after running "nc host port" in the command line to receive the flag from the server.
![alt text](3_paste_internal_state_in_cmd/images/Server_Output_Flag.png)

---

## Acknowledgments
This CTF challenge was inspired by the vulnerability of Dual Elliptic Curve Pseudo-Random Number Generators, specifically the exploit discovered by Dan Shumlow and Niels Ferguson to obtain the internal state of the PRNG.
Special thanks to Anton Kueltz and David Hacker (dmhacker) for publishing their own proof of concept implementation to demonstrate this backdoor exploit on the Dual Elliptic Curve PRNG.
(https://github.com/AntonKueltz/dual-ec-poc/tree/master)
(https://github.com/dmhacker/dual-ec-drbg/tree/master)

---

**Prepared by:** Serban Alin Caia
**Date:** 2025/02/18

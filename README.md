# Chall - Your Challenge Title

> A brief description of the challenge

## Type

- [ ] **OFF**line
- [X] **ON**line

## Designer(s)

- Ada Lovelace
- Barbara Liskov

## Description

A high-level overview intended to clarify the concept and intuition behind the challenge, outlining its educational
goals and the skills it aims to test in participants.

**IMPORTANT:** This description will **NOT** be shared with participants.

## Category(ies)

- `pwn`
- `re`
- `web`
- `stegano`
- `env`
- `crypto`
- `osint`
- `web3`
- `ai`
- `android`
- `auto`
- `misc`

---

# Project Structure

## 1. HACKME.md

- **[HACKME.md](HACKME.md)**: A teaser or description of the challenge to be shared with participants (in CTFd).

## 2. Source Code

- **[source/README.md](source/README.md)**: Comprehensive instructions on how to have a running instance of your
  challenge from the source.
  If your project includes multiple subprojects, please consult us (Anis and Hugo).
- **[source/*](source/)**: Your source code.

## 3. Offline Artifacts [OPTIONAL]

> **NOTE:** This directory is optional for online challenges. However, if offline artifacts need to be provided as well, 
> they should be placed here.

- **[offline-artifacts/*](offline-artifacts/)**: All files intended to be downloaded by participants
  (e.g., a flagless version of the running binary executable of a pwn challenge).
  For large files (exceeding 100 MB), please consult us (Anis and Hugo).

## 4. Solution

- **[solution/README.md](solution/README.md)**: A detailed writeup of the working solution.
- **[solution/FLAGS.md](solution/FLAGS.md)**: A single markdown file listing all (up-to-date) flags.
- **[solution/*](solution/)**: Any additional files or code necessary for constructing a reproducible solution for the
  challenge (e.g., `PoC.py`, `requirement.txt`, etc.).

## 5. Dockerization

> **NOTE:** For deployment on @Hack's infrastructure, online challenges must be containerized.
> However, this requirement does not apply during the early stages of challenge development, so do not hesitate to start
> building your online challenge if you are unfamiliar with containerization.
> We (Anis and Hugo) will take care of it.

- **[source/Dockerfile](source/Dockerfile)**: Needed for building a containerized image of the online challenge.
- **[source/docker-compose.yml](source/docker-compose.yml)**: Needed for a configuration-free run of the online
  challenge
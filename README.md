# @HACK 2025: Dual Duel

> Authored by [Alin](https://github.com/serbancaia).

- **Category**: `Crypto`
- **Value**: `250 points`
- **Tags**: `tcp`

> Jester, during his research, dabbled with a few Pseudo-Random Number Generators.
> 
> He became intrigued by this particular one. Can you figure out why?
> 

## Access a dockerized instance

Run challenge container using docker compose
```
docker compose up -d
```
Connect to the TCP socket (e.g., using nc command)
```
nc localhost 52004 
```
<details>
<summary>
How to stop/restart challenge?
</summary>

To stop the challenge run
```
docker compose stop
```
To restart the challenge run
```
docker compose restart
```

</details>


## Reveal Flag

Did you try solving this challenge?
<details>
<summary>
Yes
</summary>

Did you **REALLY** try solving this challenge?

<details>
<summary>
Yes, I promise!
</summary>

Flag: `ATHACKCTF{Sn0wden_walk3d_thr0ugh_the_Shumlow_Ferguson_backd0or}`

</details>
</details>


---

## About @HACK
[@HACK](https://athackctf.com/) is an annual CTF (Capture The Flag) competition hosted by [HEXPLOIT ALLIANCE](https://hexploit-alliance.com/) and [TECHNATION](https://technationcanada.ca/) at Concordia University in Montreal, Canada.

---
[Check more challenges from @HACK 2025](https://github.com/athack-ctf/AtHackCTF-2025-Challenges).
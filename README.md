<div align="center">
  <img src="./assets/hero.svg" alt="Le Minh Anh — data engineer" width="100%" />
</div>

<br/>

<table>
<tr>
<td width="58%" valign="top">

### currently building

I work around **streaming systems, lakehouse architecture, and data platforms** — mostly the parts that need to remain understandable long after the first successful demo.

My default question is not *“can this scale?”* but *“can someone still reason about this at 3 a.m.?”*

</td>
<td width="42%" valign="top">

### operating surface

`python` · `spark` · `kafka` · `debezium`  
`airflow` · `dbt` · `trino`  
`iceberg` · `hudi` · `kubernetes`

</td>
</tr>
</table>

<details>
<summary><b>open the stack map</b> — what I tend to reach for and why</summary>
<br/>

| layer | tools | what I care about |
|---|---|---|
| ingest | Debezium, Kafka | ordering, replay, observability |
| compute | Spark | deterministic transforms, operational simplicity |
| orchestration | Airflow | recoverability, clear dependency boundaries |
| modeling | dbt | readable transformations, contract-like interfaces |
| storage | Iceberg, Hudi | open formats, evolution, time travel |
| query | Trino | one access layer across heterogeneous storage |
| runtime | Kubernetes | repeatable operations without hiding failure modes |

</details>

<br/>

## recent work

<!-- recent-projects:start -->
**[kufi-e-wallet-with-hyperledger-chain-cli](https://github.com/lhem43/kufi-e-wallet-with-hyperledger-chain-cli)**  
<sub>[15 Aug 2026](https://github.com/lhem43/kufi-e-wallet-with-hyperledger-chain-cli/commit/bdfea1c199b93b92500c69115a281132d19dc0b4) · docs: polish project README and architecture overview</sub>
<!-- recent-projects:end -->

<sub>auto-sorted by latest public commit</sub>

<br/>

---

<sub>Prefer small interfaces, explicit failure modes, boring production.</sub>

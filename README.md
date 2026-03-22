# 📚 Arxiv Agent & Science of Science Papers

[![Daily Paper Update](https://github.com/liu-yi-xuan/arxiv-agent-science-of-science/actions/workflows/daily_update.yml/badge.svg)](https://github.com/liu-yi-xuan/arxiv-agent-science-of-science/actions/workflows/daily_update.yml)

> A curated, auto-updated collection of research papers on **AI Agents** and **Science of Science**, fetched daily from ArXiv with TLDRs and smart classification.

---

## 🔖 Categories

| Category | Description |
|----------|-------------|
| 🤖 **LLM Agents** | Large language model-based autonomous agents, tool use, planning |
| 🧠 **Multi-Agent Systems** | Cooperation, communication, and coordination among multiple agents |
| 🔬 **Science of Science** | Meta-research, scientometrics, research dynamics, citation analysis |
| 🛠️ **Agent Frameworks & Benchmarks** | Evaluation, benchmarks, and frameworks for agent systems |
| 📊 **Research Analytics** | Quantitative analysis of scientific output, trends, and impact |

---

## 📅 Daily Updates

<!-- DAILY_UPDATES_START -->
*Updates will appear here automatically.*
<!-- DAILY_UPDATES_END -->

---

## ⭐ Classic & Notable Papers

### 🤖 LLM Agents

| Date | Title | TLDR |
|------|-------|------|
| 2023-03 | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) | Uses ChatGPT as a controller to orchestrate existing AI models on HuggingFace for solving complex AI tasks through planning, model selection, and execution. |
| 2023-03 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | Introduces verbal self-reflection as a reinforcement signal, enabling LLM agents to learn from mistakes through natural language feedback rather than weight updates. |
| 2023-05 | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | First LLM-powered lifelong learning agent in Minecraft that builds a reusable skill library and continuously explores and learns new capabilities. |
| 2023-08 | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) | A framework enabling development of LLM applications using multiple conversable agents that can collaborate through multi-turn conversations. |
| 2023-10 | [OpenAgents: An Open Platform for Language Agents in the Wild](https://arxiv.org/abs/2310.10634) | Deploys three real-world agents (data, plugin, web) for practical daily use, bridging the gap between agent research and everyday users. |
| 2024-02 | [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456) | A framework for building generalist agents that can interact with any OS element (apps, terminal, files) and self-improve through experience. |
| 2024-03 | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) | Designs agent-computer interfaces that enable LLMs to autonomously fix real GitHub issues, achieving strong results on SWE-bench. |
| 2024-05 | [AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151) | A framework for training generally-capable LLM agents across diverse interactive environments with a trajectory-driven evolution approach. |

### 🧠 Multi-Agent Systems

| Date | Title | TLDR |
|------|-------|------|
| 2023-05 | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | Creates a town of 25 AI agents with memories and reflections that exhibit believable individual and social behaviors in an interactive sandbox. |
| 2023-07 | [Communicative Agents for Software Development (ChatDev)](https://arxiv.org/abs/2307.07924) | Structures software development as a multi-agent chat chain where AI agents play roles (CEO, CTO, programmer, tester) to collaboratively build software. |
| 2023-08 | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) | Encodes human SOPs into multi-agent collaboration, assigning specialized roles (PM, architect, engineer) with structured outputs to reduce hallucination. |
| 2024-02 | [More Agents Is All You Need](https://arxiv.org/abs/2402.05120) | Shows that simply sampling multiple LLM agents and using majority voting can substantially improve performance on diverse tasks. |

### 🔬 Science of Science

| Date | Title | TLDR |
|------|-------|------|
| 2018-03 | [Science of Science (Dashun Wang et al.)](https://doi.org/10.1126/science.aao0185) | Landmark review establishing the field — covers universal patterns in how scientists make discoveries, collaborate, and careers unfold. |
| 2019-10 | [The Science of Science: From the Perspective of Complex Systems](https://doi.org/10.1016/j.physrep.2017.10.001) | Comprehensive review framing scientific enterprise as a complex system, analyzing collaboration networks, citation dynamics, and knowledge diffusion. |
| 2021-06 | [Quantifying the Dynamics of Failure Across Science, Startups, and Security](https://doi.org/10.1038/s41586-019-1725-y) | Uncovers a universal pattern — early failures followed by eventual success — across NIH grants, startups, and terrorist attacks. |
| 2023-05 | [Papers with Code: A Leaderboard for Machine Learning](https://arxiv.org/abs/2304.00720) | Analyzes how open benchmarks and code sharing have accelerated ML research progress and reproducibility. |
| 2023-11 | [Large Language Models for Science: A Survey](https://arxiv.org/abs/2312.07622) | Surveys how LLMs are transforming scientific discovery across domains — from literature analysis to hypothesis generation and experimental design. |
| 2024-04 | [The Transformation of Science and its Societal Impact (AI for Science)](https://arxiv.org/abs/2403.19748) | Examines how AI is reshaping the scientific method itself and what it means for the future of research and discovery. |

### 📊 Research Analytics & Scientometrics

| Date | Title | TLDR |
|------|-------|------|
| 2015-05 | [Prediction of Highly Cited Papers (Xiao et al.)](https://doi.org/10.1016/j.joi.2016.05.002) | Develops features and models to predict which papers will become highly cited, revealing early signals of impact. |
| 2019-04 | [Measuring the Evolution of a Scientific Field through Citation Frames](https://arxiv.org/abs/1903.09951) | Introduces citation intent classification to track how the role and framing of cited works changes over time. |
| 2023-09 | [Can Large Language Models Provide Useful Feedback on Research Papers?](https://arxiv.org/abs/2310.01783) | Evaluates GPT-4's ability to generate peer review-like feedback, finding substantial overlap with human reviewer comments. |

---

## 🏗️ Project Structure

```
├── README.md              # This file — auto-updated daily
├── fetch_papers.py        # ArXiv paper fetcher + classifier + TLDR generator
├── papers/                # Archive of daily paper fetches (JSON)
├── .github/workflows/     # GitHub Actions for daily automation
└── requirements.txt       # Python dependencies
```

## 🚀 How It Works

1. **Daily at 08:00 UTC**, a GitHub Action triggers `fetch_papers.py`
2. The script queries ArXiv for recent papers matching our topics
3. Papers are classified into categories and a TLDR is generated
4. The README is auto-updated with the day's findings
5. Changes are committed and pushed automatically

## 📝 Contributing

Found a great paper that should be in the curated list? Open an issue or PR!

## 📜 License

MIT

# Agent Fundamentals

This project demonstrates the core foundations of **AI Agents** using a simple multi-agent pipeline.

It is built as a learning exercise to understand how agentic systems work beyond basic chatbots.

---

# What is an AI Agent?

An AI Agent is a system that:

- **Perceives** information
- **Reasons** about what to do
- **Acts** to achieve a goal

This is often called the:

> **Perception -> Reasoning -> Action Loop**

Unlike chatbots, agents are goal-driven and role-oriented.

---

# Agent vs Chatbot vs Pipeline

## Chatbot
- Reactive
- Responds to immediate input
- Minimal memory
- No long-term goals

Example: FAQ bots

---

## Pipeline
- Fixed sequence of steps
- Deterministic flow
- No autonomy
- No reasoning

Example: ETL pipelines

---

## AI Agent
- Autonomous
- Maintains goals
- Uses memory
- Adapts behavior
- Can use tools
- Role-based

Example: Research agents, coding agents, planners

---

# Core Concepts Implemented

## Role Isolation
Each agent has a strict role and does only one job.

| Agent | Responsibility |
|------|----------------|
| Research Agent | Gather raw information |
| Summarizer Agent | Condense information |
| Answer Agent | Produce final response |

This prevents overlap and improves reliability.

---

## System Prompts
Each agent is controlled by a system prompt that defines:

- Role
- Boundaries
- Output format
- Behavior rules

System prompts act as the **personality + rules** of an agent.

---

## Message-Based Communication
Agents communicate using structured messages.

Flow:

User  
- Research Agent  
- Summarizer Agent  
- Answer Agent  
- User

This mimics real multi-agent systems.

---

## Memory Window
Each agent maintains a short-term memory window.

Purpose:
- Maintain context
- Enable coherent responses
- Limit token usage

Typical size: 5–20 messages  
(Current project uses **10**)

---

##  ReAct Pattern (Reason + Act)
Agents often follow:

1. Reason about task
2. Take action
3. Observe result
4. Repeat if needed

This pattern enables dynamic problem solving.

---



# AutoStream - Social-to-Lead Conversational AI Agent

## Project Overview

This project is a Conversational AI Agent built for a fictional SaaS company called AutoStream, a platform that provides automated video editing tools for content creators.

The goal of the agent is to convert user conversations into qualified business leads by understanding intent, answering product-related queries using a local knowledge base (RAG), identifying high-intent users, and triggering lead capture through a mock API.

This project was developed as part of the Machine Learning Intern Assignment for ServiceHive (Inflx).

---

## Features

### Intent Detection

The agent classifies user input into three categories:

- Casual Greeting
- Product / Pricing Inquiry
- High-Intent Lead

Examples:

- "Hi" → Greeting
- "Tell me about your pricing" → Inquiry
- "I want to subscribe to the Pro plan" → High-Intent Lead

---

### RAG-Based Knowledge Retrieval

The agent uses a local JSON knowledge base to answer:

- Pricing details
- Plan features
- Refund policy
- Support availability

This avoids hardcoded responses and simulates Retrieval-Augmented Generation (RAG).

---

### Lead Capture Tool Execution

When a user shows high purchase intent, the agent collects:

- Name
- Email
- Creator Platform

Only after collecting all required details, the system triggers:

```python
mock_lead_capture(name, email, platform)
# Project Context - Interactive Learner

## Goal
A personal learning platform where I quickly save interesting topics I discover daily.
The LLM enriches the content and breaks it into multiple swipeable cards (like Instagram Reels).

## Core Behavior
- One topic input → LLM generates multiple cards
- New topic's cards are APPENDED to the existing feed, never overwrite
- LLM uses web search to enrich content with latest/accurate information

## Input
- Topic name
- Short description (optional)
- Blog URL (optional)

## Output
- Multiple beautified swipeable learning cards per topic
- Scrollable vertical feed (reel-style)

## Tech Stack
- Frontend: React
- Backend: Django + Django REST Framework
- LLM Provider: Gemini
- Web Search: Tavily API
- Database: PostgreSQL
- Auth: django-allauth (Google OAuth + Email OTP passwordless)
- JWT: djangorestframework-simplejwt

## Auth Flow
- Primary: Google OAuth (gets email from Google)
- Fallback: Email + OTP (passwordless, no passwords stored)
- Both flows issue JWT tokens for React ↔ Django communication
- Email is the common identifier across both auth methods

## Project Structure
(fill this as you build)

## Key Decisions
- Cards are appended, not overwritten
- One topic = multiple cards
- Each user has their own private feed
- Passwordless auth (no passwords stored)
- Web search grounds LLM responses to avoid hallucination
- Backend and frontend are separate (monorepo but independent deployment)

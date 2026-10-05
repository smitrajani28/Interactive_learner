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
- Dynamic category bar at top (filters feed by category)
- Topic index (thumbnail navigation to jump to any topic)

## LLM JSON Output Structure
```json
{
  "topic": "Machine Learning Basics",
  "category": "Machine Learning",
  "total_cards": 5,
  "cards": [
    {
      "card_number": 1,
      "title": "What is Machine Learning?",
      "content": "...",
      "key_takeaway": "ML learns patterns from data without being explicitly programmed",
      "resources": [
        {
          "title": "ML Crash Course by Google",
          "url": "https://developers.google.com/machine-learning/crash-course"
        }
      ]
    }
  ]
}
```

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
- Each topic has a category (e.g. ML, React, Node)
- Categories are dynamic — appear as topics are added
- Each card has a key takeaway and optional supporting resources
- Multiple resources per card → show selection modal on frontend
- Topic index acts as thumbnail navigation across the feed

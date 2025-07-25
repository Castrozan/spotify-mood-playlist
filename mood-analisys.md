# Mood Calculation System

The Taranify API uses a three-dimensional mood assessment system based on psychological research. The mood is calculated using three key dimensions:

## 1. Valence (V) - Happiness Level
**Question:** "Select the option that best describes your current happiness level."

- 😞 **Deeply Unhappy** (0.1): Very sad, nothing is fun
- 😔 **Somewhat Unhappy** (0.3): A bit sad, not everything is going well
- 😐 **Not happy, Nor Unhappy** (0.5): Feeling okay, not too happy, not sad either
- 🙂 **Somewhat Happy** (0.7): Mostly feeling good and happy with small things
- 😄 **Ecstatically Happy** (0.9): Extremely happy, feeling amazing about everything

## 2. Energy (E) - Energy Level
**Question:** "How energetic are you right now?"

- 😴 **Exhausted** (0.1): Completely drained, little to no energy left
- 🚶 **Low Energy** (0.3): A bit weak, finding even easy tasks hard
- 🏃 **Moderate Energy** (0.5): Having enough energy for daily stuff
- 🕺 **High Energy** (0.7): Very lively, ready for hard tasks
- 🚀 **Full of Life & Energy** (0.9): Super energetic, I can do anything happily

## 3. Dominance (D) - Control/Power Level
**Question:** "How dominant do you feel right now?"

- 🍂 **Powerless** (0.1): You can't control anything in your life
- 🌱 **Somewhat Powerless** (0.3): A bit in control, but not much
- ☯️ **Not Powerless, Nor Dominant** (0.5): Balance between controlling and being controlled
- 💪 **Somewhat Powerful** (0.7): Mostly in charge of things in your life
- 👑 **Completely Dominant** (0.9): Totally in control, you can make anything happen

## How It Works in Our Application

In our color-based application, we use default values:
- `userValence`: 0.5 (neutral happiness)
- `userEnergy`: 0.7 (high energy)
- `userDominance`: 0.7 (somewhat powerful)

The API then combines these values with the color selections to determine:
- **moodText**: A descriptive phrase like "motivated and bold"
- **moodIntensity**: A percentage (0-100%) indicating the strength of the mood

The color choices influence these base mood dimensions, creating personalized playlist recommendations that match both the user's psychological state and color preferences.


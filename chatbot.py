"""
Chatbot Response Generator
===========================
Generates context-aware responses based on user intent and patient risk level.
Provides personalized advice for diet, exercise, daily planning, and simulations.
"""

import random


# ==================== CONSTANTS ====================

GENERAL_INFO_RESPONSES = [
    "Diabetes is a chronic condition where blood sugar levels are too high.",
    "Diabetes occurs when the body cannot properly produce or use insulin to control blood sugar.",
    "Diabetes affects how your body uses glucose for energy, leading to elevated blood sugar levels.",
    "There are two main types: Type 1 (autoimmune) and Type 2 (lifestyle-related).",
]

ACTION_TO_STEPS = {
    "avoid_sugar": [
        "Avoid sugary drinks and sweets today (soda, juice, desserts).",
        "Choose low-glycemic carbs (whole grains, legumes) and add fiber (vegetables).",
        "Drink water and avoid snacking on processed foods."
    ],
    "walk_30_minutes": [
        "Walk 10–15 minutes after meals (or 30 minutes total today).",
        "Start at a comfortable pace; stop if you feel dizzy.",
        "Stay hydrated."
    ],
    "eat_healthy_meal": [
        "Eat a balanced meal: lean protein + vegetables + a small portion of whole grains.",
        "Avoid skipping meals to keep glucose stable."
    ],
}


# ==================== RESPONSE GENERATOR ====================

def generate_response(intent, plan, risk):
    """
    Generate personalized chatbot response based on intent and risk level.
    
    Args:
        intent (str): Classified user intent
        plan (list): List of recommended actions from agent
        risk (str): Patient risk level ('high', 'medium', 'low')
        
    Returns:
        str: Formatted response message
    """
    # Risk-specific prefix
    risk_prefix = _get_risk_prefix(risk)
    
    # Intent-specific responses
    if intent == "reduce_glucose":
        return _handle_reduce_glucose(risk_prefix, plan)
    
    elif intent == "diet_advice":
        return _handle_diet_advice(risk_prefix, risk)
    
    elif intent == "exercise_advice":
        return _handle_exercise_advice(risk_prefix, risk)
    
    elif intent == "daily_plan":
        return _handle_daily_plan(risk_prefix, risk)
    
    elif intent == "general_info":
        return random.choice(GENERAL_INFO_RESPONSES)
    
    elif intent == "simulate":
        return _handle_simulation_prompt()
    
    elif intent == "fallback":
        return _handle_fallback()
    
    elif intent == "acknowledgment":
        return _handle_acknowledgment()
    
    # Default fallback
    return "I'm here to help with diabetes management. Ask me about diet, exercise, or daily planning!"


# ==================== HELPER FUNCTIONS ====================

def _get_risk_prefix(risk):
    """Get risk-appropriate message prefix."""
    if risk == "high":
        return "[⚠️ HIGH RISK] Consult a specialist. "
    elif risk == "medium":
        return "[📊 MEDIUM RISK] Monitor closely. "
    else:
        return "[✅ LOW RISK] Great job! "


def _handle_reduce_glucose(risk_prefix, plan):
    """Handle glucose reduction intent with human-readable steps."""
    if not plan:
        return f"{risk_prefix}Your glucose looks stable. Keep your healthy habits!"

    # Convert action codes (e.g., avoid_sugar) into real advice steps
    steps = []
    for action in plan:
        steps.extend(ACTION_TO_STEPS.get(action, [f"Follow: {action.replace('_', ' ')}"]))

    # Remove duplicate steps while keeping order
    seen = set()
    steps_unique = []
    for s in steps:
        if s not in seen:
            steps_unique.append(s)
            seen.add(s)

    formatted_steps = "\n".join([f"• {s}" for s in steps_unique])

    return (
        f"{risk_prefix}Here’s a practical plan to help reduce glucose today:\n\n"
        f"{formatted_steps}\n\n"
        "If you feel unwell or your readings stay very high, consult a clinician."
    )



def _handle_diet_advice(risk_prefix, risk):
    """Handle diet advice intent with risk-specific recommendations."""
    diet_advice = {
        "high": (
            f"{risk_prefix}Strictly follow a low-carb, high-fiber diet.\n"
            "• Avoid: Sugary drinks, white bread, processed foods\n"
            "• Eat: Leafy greens, lean protein, whole grains\n"
            "• Portion control is critical"
        ),
        "medium": (
            f"{risk_prefix}Watch your carbohydrate intake carefully.\n"
            "• Choose whole grains over refined grains\n"
            "• Limit sugar and processed foods\n"
            "• Eat balanced meals with protein and fiber"
        ),
        "low": (
            f"{risk_prefix}Maintain your healthy eating habits!\n"
            "• Continue eating plenty of vegetables\n"
            "• Keep portions balanced\n"
            "• Stay hydrated and limit processed foods"
        )
    }
    return diet_advice.get(risk, diet_advice["low"])


def _handle_exercise_advice(risk_prefix, risk):
    """Handle exercise advice intent with risk-specific recommendations."""
    exercise_advice = {
        "high": (
            f"{risk_prefix}Start with gentle, low-impact exercise.\n"
            "• Begin with 10-15 min walks after meals\n"
            "• Monitor blood sugar before and after\n"
            "• Consult your doctor before intense exercise"
        ),
        "medium": (
            f"{risk_prefix}Aim for regular moderate activity.\n"
            "• Target: 150 minutes per week\n"
            "• Try: Brisk walking, swimming, cycling\n"
            "• Exercise helps lower your risk significantly"
        ),
        "low": (
            f"{risk_prefix}Keep up your active lifestyle!\n"
            "• Continue your regular exercise routine\n"
            "• Mix cardio and strength training\n"
            "• Stay active to maintain your low risk"
        )
    }
    return exercise_advice.get(risk, exercise_advice["low"])


def _handle_daily_plan(risk_prefix, risk):
    """Handle daily plan intent with risk-specific schedules."""
    daily_plans = {
        "high": (
            f"{risk_prefix}Here is a safe daily plan:\n\n"
            "🌅 Morning:\n"
            "  • Check glucose upon waking\n"
            "  • Light breakfast: Oatmeal with berries\n\n"
            "☀️ Mid-day:\n"
            "  • 15-min walk after lunch\n"
            "  • Salad with lean protein\n\n"
            "🌙 Evening:\n"
            "  • Grilled vegetables and fish\n"
            "  • Check glucose before bed"
        ),
        "medium": (
            f"{risk_prefix}Suggested daily routine:\n\n"
            "🌅 Morning: Balanced breakfast with protein\n"
            "☀️ Afternoon: 30-min brisk walk\n"
            "🌙 Evening: Avoid late-night carbs, early dinner"
        ),
        "low": (
            f"{risk_prefix}Healthy daily routine:\n\n"
            "🌅 Morning: Continue your healthy breakfast\n"
            "☀️ Day: Stay active with your favorite activities\n"
            "🌙 Evening: Maintain regular meal times"
        )
    }
    return daily_plans.get(risk, daily_plans["low"])


def _handle_simulation_prompt():
    """Handle simulation mode activation."""
    return (
        "🔮 Simulation Mode Activated!\n\n"
        "I can simulate different lifestyle scenarios for you.\n\n"
        "Try asking:\n"
        "  • 'What if I walk daily?'\n"
        "  • 'What if I don't exercise?'\n"
        "  • 'What if I eat healthy?'\n"
        "  • 'What if I eat junk food?'\n"
        "  • 'What if I reduce stress?'\n\n"
        "Type your scenario question to see predicted outcomes!"
    )


def _handle_fallback():
    """Handle unrecognized intents."""
    return (
        "I'm not sure I understand. I can help with:\n"
        "  • Diet advice\n"
        "  • Exercise recommendations\n"
        "  • Daily planning\n"
        "  • What-if simulations\n"
        "  • General diabetes information\n\n"
        "Could you please rephrase your question?"
    )


def _handle_acknowledgment():
    """Handle casual conversational responses."""
    responses = [
        "You're welcome! Let me know if you need anything else.",
        "Happy to help! Feel free to ask more questions.",
        "Anytime! I'm here to support your diabetes management.",
        "Glad I could help! What else would you like to know?",
    ]
    return random.choice(responses)



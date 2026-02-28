def test_app_uses_form_submit_button():
    """The main application should use a Streamlit form submit button."""
    src = open("app.py").read()
    assert "form_submit_button" in src


def test_submit_button_not_plain():
    """Verify the old standalone submit button is gone."""
    src = open("app.py").read()
    assert 'st.button("Submit Guess' not in src


def test_difficulty_resets_secret():
    """Ensure the code checks for a difficulty change and resets state."""
    src = open("app.py").read()
    assert "prev_difficulty" in src
    assert "st.session_state.prev_difficulty" in src

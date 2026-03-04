import pytest
from pages.drag_and_drop_page import DragAndDropPage


def test_drag_and_drop(page: Page):
    """
    Test verifies drag-and-drop between columns A and B, ensuring labels swap positions
    after dragging and return to original positions when dragged back.
    """
    drag_and_drop_page = DragAndDropPage(page)
    drag_and_drop_page.goto()
    column_a = drag_and_drop_page.column_a
    column_b = drag_and_drop_page.column_b

    # Record the initial positions of labels in columns A and B
    label_a_initial_position = drag_and_drop_page.label_a_position()
    label_b_initial_position = drag_and_drop_page.label_b_position()

    # Drag column A to column B
    column_a.drag_to(column_b)

    # Capture the positions after the first drag
    label_a_current_position = drag_and_drop_page.label_a_position()
    label_b_current_position = drag_and_drop_page.label_b_position()
    assert label_a_current_position == label_b_initial_position, \
        "Label A should have moved to Column B's initial position."
    assert label_b_current_position == label_a_initial_position, \
        "Label B should have moved to Column A's initial position."

    # Drag column B back to column A
    column_b.drag_to(column_a)

    # Capture positions after dragging back
    label_a_current_position = drag_and_drop_page.label_a_position()
    label_b_current_position = drag_and_drop_page.label_b_position()
    assert label_a_current_position == label_a_initial_position, \
        "Label A should be back to its original position."
    assert label_b_current_position == label_b_initial_position, \
        "Label B should be back to its original position."


def test_drag_and_drop_reversed(page: Page):
    """
    Similar to the first test, but starts by dragging label B to label A,
    then drags back, verifying the labels swap and revert positions.
    """
    drag_and_drop_page = DragAndDropPage(page)
    drag_and_drop_page.goto()
    column_a = drag_and_drop_page.column_a
    column_b = drag_and_drop_page.column_b

    # Record the initial positions of labels in columns A and B
    label_a_initial_position = drag_and_drop_page.label_a_position()
    label_b_initial_position = drag_and_drop_page.label_b_position()

    # Drag column B to column A
    column_b.drag_to(column_a)

    # Capture the positions after the first drag
    label_a_current_position = drag_and_drop_page.label_a_position()
    label_b_current_position = drag_and_drop_page.label_b_position()
    assert label_a_current_position == label_b_initial_position, \
        "Label A should have moved to Column B's initial position."
    assert label_b_current_position == label_a_initial_position, \
        "Label B should have moved to Column A's initial position."

    # Drag column A back to column B
    column_a.drag_to(column_b)

    # Capture positions after dragging back
    label_a_current_position = drag_and_drop_page.label_a_position()
    label_b_current_position = drag_and_drop_page.label_b_position()
    assert label_a_current_position == label_a_initial_position, \
        "Label A should be back to its original position."
    assert label_b_current_position == label_b_initial_position, \
        "Label B should be back to its original position."

import pytest

from .models import Board, Task


@pytest.mark.django_db
def test_cascading_delete_does_not_cause_recursion_error(board_factory, task_factory):
    """
    Tests that deleting a parent object with ranked children
    does not cause a RecursionError.
    """
    board = board_factory(name="Project Phoenix")
    task_factory(name="Gather requirements", board=board)
    task_factory(name="Design mockups", board=board)
    task_factory(name="Develop feature", board=board)

    assert board.tasks.count() == 3

    try:
        board.delete()
    except RecursionError:
        pytest.fail("Deleting the parent object caused a RecursionError.")

    assert not Board.objects.filter(pk=board.pk).exists()
    assert Task.objects.count() == 0
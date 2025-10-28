import typer
from task_manager import TaskManager

app = typer.Typer(help="A simple CLI TODO application powered by Typer.")
manager = TaskManager()

@app.command(name="add")
def add(description: str = typer.Argument(..., help="Description of the task to add")):
    """Add a new task."""
    try:
        task = manager.add_task(description)
        typer.echo(f"Task added: {task.id} | {task.description}")
    except ValueError as e:
        typer.echo(f"Error: {e}")

@app.command(name="list")
def list_tasks():
    """List all tasks."""
    tasks = manager.get_all_tasks()
    if not tasks:
        typer.echo("No tasks available.")
        return
    for t in tasks:
        status = "Completed" if t.completed else "Incomplete"
        typer.echo(f"{t.id} | {status} | {t.description}")

@app.command(name="complete")
def complete(task_id: str):
    """Mark a task as completed."""
    ok = manager.mark_completed(task_id)
    if ok:
        typer.echo("Task marked as completed.")
    else:
        typer.echo("Task not found.")

@app.command(name="delete")
def delete(task_id: str):
    """Delete a task."""
    ok = manager.delete_task(task_id)
    if ok:
        typer.echo("Task deleted.")
    else:
        typer.echo("Task not found.")

@app.command(name="info")
def info():
    """Show app info."""
    typer.echo("CLI TODO Application — Typer Version")


if __name__ == "__main__":
    app()

from pydantic import BaseModel, field_validator, Field, ValidationError


class ResourceRequests(BaseModel):
    id: int
    project_tasks_resource_id: int
    volume: str
    cost: str
    batch_number: None | int
    batch_parent_request_id: None | int
    is_over_budget: bool
    created_at: int
    updated_at: int
    user_id: int
    needed_at: int
    created_by: int


def validate_json(incoming_json, schema_json):
    try:
        schema_json(**incoming_json)
        return True
    except ValidationError as e:
        return e.errors()





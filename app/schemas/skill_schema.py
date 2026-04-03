from pydantic import BaseModel, field_validator

class SkillInput(BaseModel):
    skills: str

    @field_validator("skills")
    def validate_skills(cls, value):
        if not value or len(value.strip()) < 3:
            raise ValueError("Skills must be at least 3 characters long")
        return value.lower()
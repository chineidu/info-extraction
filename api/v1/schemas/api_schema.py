from pydantic import BaseModel


class APIConfigSchema(BaseModel):
    """API Configurations."""

    API_VERSION_STR: str
    API_FULL_VERSION: str
    PROJECT_NAME: str


class ConfigVars(BaseModel):
    """Main configuration object."""

    api_config_schema: APIConfigSchema

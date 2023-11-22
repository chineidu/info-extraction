from pydantic import BaseModel


class FEConfigSchema(BaseModel):
    """API Configurations."""

    API_VERSION_STR: str
    HOST: str
    PORT: int
    PREFIX: str


class ConfigVars(BaseModel):
    """Main configuration object."""

    fe_config_schema: FEConfigSchema

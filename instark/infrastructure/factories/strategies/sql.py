sql = {
    # --- REPOSITORIES ---
    "SqlParser": {
        "method": "sql_query_parser"
    },
    "ConnectionManager": {
        "method": "sql_connection_manager"
    },
    "TransactionManager": {
        "method": "sql_transaction_manager",
    },
    "ChannelRepository": {
        "method": "sql_channel_repository"
    },
    "DeviceRepository": {
        "method": "sql_device_repository"
    },
    "MessageRepository": {
        "method": "sql_message_repository"
    },
    "SubscriptionRepository": {
        "method": "sql_subscription_repository"
    },
    # --- SUPPLIERS ---
    "TenantSupplier": {
        "method": "schema_tenant_supplier"
    },
    "SetupSupplier": {
        "method": "schema_setup_supplier"
    },
}

sql = {
    # --- REPOSITORIES ---
    "SqlParser": {
        "method": "sql_query_parser"
    },
    # --- MANAGERS ---
    "ConnectionManager": {
        "method": "sql_connection_manager"
    },
    "TransactionManager": {
        "method": "sql_transaction_manager",
    },
    # --- REPOSITORIES ---
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
    "MigrationSupplier": {
        "method": "schema_migration_supplier"
    },
    # --- SERVICE ---
    "DeliveryService": {
        "method": "memory_delivery_service"
    },
    # --- SERVICE ---
    # "DeliveryService": {
    #     "method": "firebase_delivery_service"
    # },
}

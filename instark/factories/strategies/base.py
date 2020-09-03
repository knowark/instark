base = {
    # --- PROVIDERS ---
    "QueryParser": {
        "method": "query_parser"
    },
    "TenantProvider": {
        "method": "standard_tenant_provider"
    },
    "AuthProvider": {
        "method": "standard_auth_provider"
    },
    "TransactionManager": {
        "method": "memory_transaction_manager"
    },
    # --- REPOSITORIES ---
    "ChannelRepository": {
        "method": "memory_channel_repository"
    },
    "DeviceRepository": {
        "method": "memory_device_repository"
    },
    "MessageRepository": {
        "method": "memory_message_repository"
    },
    "SubscriptionRepository": {
        "method": "memory_subscription_repository"
    },
    # --- MANAGERS ---
    "NotificationManager": {
        "method": "notification_manager"
    },
    "RegistrationManager": {
        "method": "registration_manager"
    },
    "SessionManager": {
        "method": "session_manager"
    },
    "SubscriptionManager": {
        "method": "subscription_manager"
    },
    # --- INFORMERS ---
    "InstarkInformer": {
        "method": "standard_instark_informer"
    },
    # --- SUPPLIERS ---
    "TenantSupplier": {
        "method": "memory_tenant_supplier"
    },
    # --- SERVICES ---
    "DeliveryService": {
        "method": "memory_delivery_service"
    },
}

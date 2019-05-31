# from flask import Flask
# from flask_restful import Api
# from ..config import Registry
# from instark.infrastructure.web.resources import (MessageResource,
#                                                   ChannelResource,
#                                                   DeviceResource,
#                                                   SubscriptionResource)
# from instark.application.repositories.message_repository import (
#     MemoryMessageRepository)
# from instark.application.repositories.channel_repository import (
#     MemoryChannelRepository)
# from instark.application.repositories.device_repository import (
#     MemoryDeviceRepository)
# from instark.application.repositories.subscription_repository import (
#     MemorySubscriptionRepository)
# from instark.application.coordinators.notification_coordinator import (
#     NotificationCoordinator)
# from instark.application.coordinators.subscription_coordinator import (
#     SubscriptionCoordinator)
# from instark.application.coordinators.registration_coordinator import (
#     RegistrationCoordinator)


# def set_routes(app: Flask, registry: Registry) -> None:

#     @app.route('/')
#     def index() -> str:
#         return 'Welcome to Instark!'

#     # Restful API
#     api = Api(app)

#     # Services
#     notification_coordinator = registry['NotificationCoordinator']
#     subscription_coordinator = registry['SubscriptionCoordinator']
#     registration_coordinator = registry['RegistrationCoordinator']

#     # Message resource
#     api.add_resource(
#         MessageResource,
#         '/register', '/signup',
#         resource_class_kwargs={
#             'notification_coordinator': notification_coordinator
#         })

#     # Channel resource
#     api.add_resource(
#         ChannelResource,
#         '/register', '/signup',
#         resource_class_kwargs={
#             'subscription_coordinator': subscription_coordinator
#         })

#     # Device resource
#     api.add_resource(
#         DeviceResource,
#         '/register', '/signup',
#         resource_class_kwargs={
#             'registration_coordinator': registration_coordinator
#         })

#     # Subscription resource
#     api.add_resource(
#         DeviceResource,
#         '/register', '/signup',
#         resource_class_kwargs={
#             'subscription_coordinator': subscription_coordinator
#         })

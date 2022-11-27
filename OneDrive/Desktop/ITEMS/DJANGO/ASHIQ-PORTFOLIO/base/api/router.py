from .view import ProfileView, ExperienceView, AboutView, LCView, MemorableMomentView, TestimonialView, WorkedClubView, ContactMeView
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('profile',ProfileView)

router.register('experience',ExperienceView)

router.register('about',AboutView)

router.register('certificate',LCView)

router.register('gallery',MemorableMomentView)

router.register('testimonial',TestimonialView)

router.register('worked-club',WorkedClubView)

router.register('contact',ContactMeView)


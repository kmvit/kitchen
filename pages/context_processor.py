from .models import ContactInformation


def contact_information(request):
	info = ContactInformation.objects.first()
	context = {
		'phone' : info.phone,
		'mobile' : info.mobile_phone,
		'email' : info.email,
		'address' : info.address,
		'instagram' : info.instagram,
		'vk' : info.vk,
	}
	return context
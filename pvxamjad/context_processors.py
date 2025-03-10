
from django.templatetags.static import static

def global_context(request):

    return {
        'site_name': 'amdxworks',
        'contact_email': 'amjadpvamd@gmail.com',
        'contact_number':'+91 7356407590',
        'meta_description': 'Get high-quality and affordable websites with domain & hosting services. I specialize in Django-based web development, graphic design, and logo creation. Contact now!',
        'meta_keywords': 'web development, affordable websites, Django websites, domain and hosting, graphic design, logo design, eCommerce websites, portfolio websites, business websites, fast web solutions,web development, website design, affordable websites, Django development, HTML CSS JavaScript, Bootstrap websites, domain and hosting services, custom web applications, eCommerce website development, business websites, portfolio websites, SEO-friendly websites, fast-loading websites, responsive web design, digital solutions, professional website builder, logo design, graphic design, branding services, web solutions, UI/UX design, full-stack development, online presence, web services, small business websites, personal websites, startup websites, creative web design',
        'meta_author': 'amdxworks',
        'og_image': request.build_absolute_uri(static('assets/imgs/avatar2.jpg')),  # Social media thumbnail
        'twitter_handle': '@',
    }
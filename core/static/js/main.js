document.addEventListener('DOMContentLoaded', function () {

    // ===== Mobile Nav Toggle =====
    const toggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (toggle && navLinks) {
        toggle.addEventListener('click', function () {
            navLinks.classList.toggle('nav-links--open');
            toggle.classList.toggle('nav-toggle--active');
        });
        navLinks.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navLinks.classList.remove('nav-links--open');
                toggle.classList.remove('nav-toggle--active');
            });
        });
    }

    // ===== Navbar Scroll Effect =====
    var navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 40) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // ===== Scroll Animations =====
    var animElements = document.querySelectorAll('[data-animate]');
    if (animElements.length > 0) {
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        animElements.forEach(function (el) {
            observer.observe(el);
        });
    }

    // ===== Toast Auto-dismiss =====
    document.querySelectorAll('.toast').forEach(function (toast) {
        setTimeout(function () {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(40px)';
            setTimeout(function () { toast.remove(); }, 400);
        }, 4500);
    });

    // ===== Smooth scroll for anchor links =====
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

});

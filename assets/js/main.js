document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');

    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('mobile');
        hamburger.classList.toggle('active');

        // Lock body scroll when menu is open
        if (navMenu.classList.contains('mobile')) {
            document.body.style.overflow = 'hidden';
            hamburger.innerHTML = '<span></span><span></span><span></span>';
            const spans = hamburger.querySelectorAll('span');
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
        } else {
            document.body.style.overflow = 'auto';
            const spans = hamburger.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });

    // Animate Stats on Scroll
    const stats = document.querySelectorAll('.stat-number');
    const animateStats = () => {
        stats.forEach(stat => {
            const target = parseInt(stat.getAttribute('data-count'));
            const current = parseInt(stat.innerText);
            const increment = target / 50;

            if (current < target) {
                stat.innerText = Math.ceil(current + increment);
                setTimeout(animateStats, 20);
            } else {
                stat.innerText = target;
            }
        });
    };

    // Intersection Observer for Stats
    const observerOptions = {
        threshold: 0.5
    };

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                statsObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const statsSection = document.querySelector('.hero-stats');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }

    // Smooth Scroll for Internal Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                if (navMenu.classList.contains('mobile')) {
                    hamburger.click();
                }
            }
        });
    });
});

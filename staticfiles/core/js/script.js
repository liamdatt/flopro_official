// FloPro - Ultra Modern Interactive JavaScript

// Enhanced Animation Controller
class AnimationController {
    constructor() {
        this.observers = [];
        this.particles = [];
        this.mousePosition = { x: 0, y: 0 };
        this.init();
    }

    init() {
        this.setupScrollAnimations();
        this.setupParticleSystem();
        this.setupMouseTracking();
        this.setupAdvancedInteractions();
        this.setupNavbarEffects();
        this.setupFormAnimations();
    }

    // Advanced Scroll Animations
    setupScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    element.classList.add('in-view');
                    
                    // Stagger animations for child elements
                    const children = element.querySelectorAll('.stagger-child');
                    children.forEach((child, index) => {
                        setTimeout(() => {
                            child.style.transform = 'translateY(0) translateX(0)';
                            child.style.opacity = '1';
                        }, index * 100);
                    });
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.querySelectorAll('.animate-on-scroll').forEach(el => {
            observer.observe(el);
        });

        this.observers.push(observer);
    }

    // Particle System (Simplified)
    setupParticleSystem() {
        const canvas = document.createElement('canvas');
        canvas.id = 'particle-canvas';
        canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:-1;opacity:0.6;';
        document.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        for (let i = 0; i < 20; i++) {
            this.particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                size: Math.random() * 2 + 1
            });
        }

        const animate = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            this.particles.forEach(p => {
                p.x += p.vx;
                p.y += p.vy;
                if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
                if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
                
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(0, 245, 255, 0.5)';
                ctx.fill();
            });
            requestAnimationFrame(animate);
        };
        animate();
    }

    // Mouse Tracking
    setupMouseTracking() {
        document.addEventListener('mousemove', (e) => {
            this.mousePosition = { x: e.clientX, y: e.clientY };
        });
    }

    // Advanced Interactions
    setupAdvancedInteractions() {
        document.querySelectorAll('.btn, .card').forEach(element => {
            element.addEventListener('mouseenter', () => {
                element.style.transform = 'translateY(-5px) scale(1.02)';
            });
            element.addEventListener('mouseleave', () => {
                element.style.transform = '';
            });
        });
    }

    // Enhanced Navbar
    setupNavbarEffects() {
        const navbar = document.querySelector('.navbar');
        let lastScrollTop = 0;

        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollTop > lastScrollTop && scrollTop > 100) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }

            if (scrollTop > 50) {
                navbar.style.background = 'rgba(10, 10, 15, 0.98)';
                navbar.style.backdropFilter = 'blur(20px)';
            } else {
                navbar.style.background = 'rgba(10, 10, 15, 0.95)';
            }

            lastScrollTop = scrollTop;
        });
    }

    // Form Animations
    setupFormAnimations() {
        const forms = document.querySelectorAll('form');
        console.log('Found forms:', forms.length);
        forms.forEach((form, index) => {
            console.log(`Form ${index}:`, form.action, form.method);
            form.addEventListener('submit', function(e) {
                console.log('Form submit event triggered!', form.action);
                // Allow native form submission; only enhance button UI
                
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn) {
                    console.log('Button found, updating UI');
                    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
                    submitBtn.disabled = true;
                } else {
                    console.log('No submit button found');
                }
            });
        });
    }
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize main animation controller
    const animationController = new AnimationController();
    
    // Store instance globally for cleanup if needed
    window.floProApp = {
        animationController,
        cleanup: () => {
            animationController.destroy();
        }
    };

    // Add animation classes to elements
    setTimeout(() => {
        document.querySelectorAll('.card, .feature-card, .service-card').forEach((card, index) => {
            card.classList.add('animate-on-scroll');
            card.style.transitionDelay = `${index * 0.1}s`;
        });
    }, 100);

    console.log('🚀 FloPro Ultra Modern Interface Initialized');
});

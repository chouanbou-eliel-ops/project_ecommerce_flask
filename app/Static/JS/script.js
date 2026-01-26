
// Gestion du bouton retour en haut (optimisé avec throttle)
const backToTopBtn = document.getElementById('backToTop');

// Fonction de throttle pour optimiser les performances
function throttle(func, delay) {
    let lastCall = 0;
    return function(...args) {
        const now = new Date().getTime();
        if (now - lastCall < delay) {
            return;
        }
        lastCall = now;
        return func(...args);
    }
}

// Afficher/masquer le bouton selon le scroll
const handleScroll = throttle(() => {
    if (window.scrollY > 300) {
        backToTopBtn.classList.add('show');
    } else {
        backToTopBtn.classList.remove('show');
    }
}, 100);

window.addEventListener('scroll', handleScroll);

// Remonter en haut avec animation fluide
backToTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    // Animation progressive personnalisée
    const scrollStep = -window.scrollY / (500 / 15);
    const scrollInterval = setInterval(() => {
        if (window.scrollY !== 0) {
            window.scrollBy(0, scrollStep);
        } else {
            clearInterval(scrollInterval);
        }
    }, 15);
    
    // Alternative avec scrollTo natif (plus fluide sur navigateurs modernes)
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

//gestion du mode d'affichage(clair/sombre)
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

if (localStorage.getItem('darkMde') === 'enable') {
    body.classList.add('dark-mode');
    themeToggle.checked = true
}

themeToggle.addEventListener('change', () =>{
    if (themeToggle.checked) {
        body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'enabled');
    } else {
        body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'disabled');
    }
});

// Animation au survol des liens dans le footer
const footerLinks = document.querySelectorAll('.footer-links a');

footerLinks.forEach(link => {
    link.addEventListener('mouseenter', function (params) {
        this.style.transition = 'all 0.3s ease';        
    });
});
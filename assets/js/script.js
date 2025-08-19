// Navbar toggle functionality for mobile
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');

if (navToggle && navMenu) {
	navToggle.addEventListener('click', () => {
		navMenu.classList.toggle('active');
	});

	// Optional: Close menu when a link is clicked (for better UX)
	document.querySelectorAll('.nav-link').forEach(link => {
		link.addEventListener('click', () => {
			navMenu.classList.remove('active');
		});
	});
}

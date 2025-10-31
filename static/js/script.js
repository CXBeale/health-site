
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

// Food Tracker functionality (only runs on food-tracker.html)
const foodInput = document.getElementById('food-input');
const addFoodBtn = document.getElementById('add-food-btn');
const foodList = document.getElementById('food-list');

if (foodInput && addFoodBtn && foodList) {
	// Load saved foods from localStorage
	let foods = JSON.parse(localStorage.getItem('foods')) || [];
	foods.forEach(food => addFoodToList(food));

	addFoodBtn.addEventListener('click', () => {
		const food = foodInput.value.trim();
		if (food) {
			foods.push(food);
			localStorage.setItem('foods', JSON.stringify(foods));
			addFoodToList(food);
			foodInput.value = '';
		}
	});

	function addFoodToList(food) {
		const li = document.createElement('li');
		li.textContent = food;
		foodList.appendChild(li);
	}
}
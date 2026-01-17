const fs = require('fs');
const path = require('path');

const requiredFiles = [
    'index.html',
    'pages/courses.html',
    'pages/modules.html',
    'pages/practice.html',
    'pages/career.html',
    'pages/about.html',
    'pages/contact.html',
    'pages/blog.html',
    'pages/dashboard.html',
    'pages/course-it-business.html',
    'assets/css/style.css',
    'assets/js/main.js'
];

let failedTests = 0;

console.log('🚀 Starting ProSpeak Website Reorganized Integrity Tests...\n');

requiredFiles.forEach(file => {
    const filePath = path.join(__dirname, '..', file);
    if (fs.existsSync(filePath)) {
        const stats = fs.statSync(filePath);
        if (stats.size > 0) {
            console.log(`✅ ${file} exists and is not empty (${stats.size} bytes)`);
        } else {
            console.log(`❌ ${file} is empty!`);
            failedTests++;
        }
    } else {
        console.log(`❌ ${file} is missing!`);
        failedTests++;
    }
});

// Check if index.html links to pages correctly
const indexContent = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
if (indexContent.includes('pages/courses.html') && indexContent.includes('assets/css/style.css')) {
    console.log('✅ index.html links updated correctly.');
} else {
    console.log('❌ index.html links NOT updated correctly.');
    failedTests++;
}

// Check sibling links in a page
const coursesContent = fs.readFileSync(path.join(__dirname, '..', 'pages/courses.html'), 'utf8');
if (coursesContent.includes('../assets/css/style.css') && coursesContent.includes('modules.html')) {
    console.log('✅ pages/courses.html links updated correctly.');
} else {
    console.log('❌ pages/courses.html links NOT updated correctly.');
    failedTests++;
}

console.log('\n-------------------------------------------');
if (failedTests === 0) {
    console.log('🔥 ALL INTEGRITY TESTS PASSED!');
    process.exit(0);
} else {
    console.log(`💥 FAILED: ${failedTests} issues found.`);
    process.exit(1);
}

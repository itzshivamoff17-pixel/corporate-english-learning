const fs = require('fs');
const path = require('path');

const pagesDir = path.join(__dirname, '..', 'pages');
const files = fs.readdirSync(pagesDir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    const filePath = path.join(pagesDir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    // Update CSS and JS paths
    content = content.replace(/href="css\/style\.css"/g, 'href="../assets/css/style.css"');
    content = content.replace(/src="js\/main\.js"/g, 'src="../assets/js/main.js"');

    // Update index.html link
    content = content.replace(/href="index\.html"/g, 'href="../index.html"');

    // List of internal page links to NOT change since they are now in the same directory
    // but the original code might have had them as root-relative.
    // Actually, in the original code they were all like href="courses.html".
    // Since they are all now in /pages/, href="courses.html" is still correct for siblings.

    fs.writeFileSync(filePath, content);
    console.log(`Updated ${file}`);
});

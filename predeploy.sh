#!/bin/bash

echo "🔒 Stashing current changes..."
git stash save "Pre-deploy stash on $(date)"

echo "✅ Switching to gh-pages..."
git checkout gh-pages

branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" != "gh-pages" ]; then
  echo "❌ Not on gh-pages branch. Aborting cleanup."
  exit 1
fi

echo "📦 Preparing clean deploy folder..."
mkdir temp-gh-pages
cp report.html temp-gh-pages/
cp index.html temp-gh-pages/

echo "🧹 Cleaning up gh-pages safely..."
rm -rf *
mv temp-gh-pages/* .
rmdir temp-gh-pages

echo "✅ Committing cleaned gh-pages..."
git add .
git commit -m "Deploy latest report to GitHub Pages"
git push origin gh-pages --force

echo "🔁 Switching back to main and restoring stash..."
git checkout main
git stash pop
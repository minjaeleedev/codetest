# Dataview Queries Reference

This file contains useful Dataview queries for analyzing and managing your problem-solving collection across multiple platforms (LeetCode, Baekjoon, Kattis, etc.).

## Basic Queries

### 1. All Problems by Platform

```dataview
TABLE platform-problem-id as "ID", title, difficulty, status, rating
FROM "LeetCode" OR "Baekjoon" OR "Kattis"
SORT platform ASC, platform-problem-id ASC
```

### 2. Problems Grouped by Platform

```dataview
TABLE rows.platform-problem-id as "Problem IDs", length(rows) as "Count"
GROUP BY platform
SORT platform ASC
```

### 3. Recent Solved Problems

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, rating
WHERE date-solved
SORT date-solved DESC
LIMIT 20
```

## Progress Tracking

### 4. Unsolved Problems

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, topics
WHERE status != "Solved" AND status != "Mastered"
SORT rating DESC, platform ASC
```

### 5. Problems by Status

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, rating
WHERE status = "Attempted"
SORT date-attempted DESC
```

### 6. Mastered Problems

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, approach, review-count
WHERE status = "Mastered"
SORT rating DESC
```

## Review and Study

### 7. Problems Due for Review

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, next-review, review-count
WHERE next-review AND next-review <= date(today)
SORT next-review ASC
```

### 8. Problems Never Reviewed

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, date-solved, rating
WHERE status = "Solved" AND review-count = 0
SORT rating DESC, date-solved ASC
```

### 9. High Difficulty Problems (Rating 8-10)

```dataview
TABLE platform, platform-problem-id as "ID", title, approach, rating, review-count
WHERE rating >= 8
SORT rating DESC, date-solved DESC
```

## Topic Analysis

### 10. Problems by Topic

```dataview
TABLE length(rows) as "Count"
FLATTEN topics as topic
GROUP BY topic
SORT length(rows) DESC
```

### 11. Problems for Specific Topic (e.g., Dynamic Programming)

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, approach, rating
WHERE contains(topics, "Dynamic Programming")
SORT rating DESC
```

### 12. Multi-Topic Problems

```dataview
TABLE platform, platform-problem-id as "ID", title, topics, rating
WHERE length(topics) >= 4
SORT length(topics) DESC, rating DESC
```

## Difficulty Analysis

### 13. Problems by Difficulty Distribution

```dataview
TABLE length(rows) as "Count"
GROUP BY difficulty
SORT difficulty DESC
```

### 14. Hard Problems on Specific Platform

```dataview
TABLE platform-problem-id as "ID", title, status, rating, approach
FROM "LeetCode"
WHERE difficulty = "Hard"
SORT rating DESC
```

### 15. Personal Rating vs Official Difficulty

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, rating, notes
WHERE rating >= 7 AND difficulty = "Easy"
SORT rating DESC
```

## Platform Statistics

### 16. Platform Summary Statistics

```dataview
TABLE
  length(rows) as "Total",
  length(filter(rows, (r) => r.status = "Solved" OR r.status = "Mastered")) as "Solved",
  length(filter(rows, (r) => r.status = "Attempted")) as "Attempted",
  length(filter(rows, (r) => r.status = "Not Started")) as "Not Started"
GROUP BY platform
SORT platform ASC
```

### 17. LeetCode Progress by Difficulty

```dataview
TABLE
  difficulty,
  length(rows) as "Total",
  length(filter(rows, (r) => r.status = "Solved" OR r.status = "Mastered")) as "Solved"
FROM "LeetCode"
GROUP BY difficulty
SORT difficulty ASC
```

### 18. Average Rating by Platform

```dataview
TABLE
  round(sum(rows.rating) / length(rows), 1) as "Avg Rating",
  length(rows) as "Total Problems"
WHERE rating
GROUP BY platform
SORT platform ASC
```

## Solution Approach Analysis

### 19. Most Common Approaches

```dataview
TABLE length(rows) as "Count", rows.platform as "Platforms"
WHERE approach
GROUP BY approach
SORT length(rows) DESC
```

### 20. Problems Using Specific Approach (e.g., Dynamic Programming)

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, rating, space-complexity
WHERE contains(approach, "Dynamic Programming") OR contains(approach, "DP")
SORT rating DESC
```

## Time-Based Analysis

### 21. Problems Solved This Month

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, rating, date-solved
WHERE date-solved >= date(today) - dur(30 days)
SORT date-solved DESC
```

### 22. Most Attempted Problems

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, attempts, status
WHERE attempts >= 3
SORT attempts DESC
```

### 23. Problem Solving Streak

```dataview
TABLE date-solved, platform, platform-problem-id as "ID", title, difficulty
WHERE date-solved
SORT date-solved DESC
LIMIT 30
```

## Similar Problems

### 24. Find Problems with Similar Problems Listed

```dataview
TABLE platform, platform-problem-id as "ID", title, similar-problems
WHERE similar-problems
SORT platform-problem-id ASC
```

## Space Complexity Analysis

### 25. Problems by Space Complexity

```dataview
TABLE platform, platform-problem-id as "ID", title, approach, space-complexity
WHERE space-complexity
GROUP BY space-complexity
SORT space-complexity ASC
```

### 26. Constant Space Solutions

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, approach, rating
WHERE contains(space-complexity, "O(1)")
SORT rating DESC
```

## Custom Views

### 27. Problems to Review Today (Combination Query)

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, rating, notes
WHERE (next-review AND next-review <= date(today)) OR (status = "Solved" AND review-count = 0 AND rating >= 7)
SORT rating DESC
```

### 28. Hardest Unsolved Problems

```dataview
TABLE platform, platform-problem-id as "ID", title, difficulty, topics, notes
WHERE status != "Solved" AND status != "Mastered" AND rating >= 7
SORT rating DESC, difficulty DESC
```

### 29. Quick Wins (Easy Problems Not Started)

```dataview
TABLE platform, platform-problem-id as "ID", title, topics, url
WHERE difficulty = "Easy" AND status = "Not Started"
SORT platform-problem-id ASC
LIMIT 10
```

### 30. Study Plan: Weak Topics

Find topics you haven't practiced much:

```dataview
TABLE length(rows) as "Count"
FLATTEN topics as topic
WHERE status = "Solved" OR status = "Mastered"
GROUP BY topic
SORT length(rows) ASC
LIMIT 10
```

## Tips for Using These Queries

1. **Customize paths**: Update `FROM "LeetCode"` to match your actual directory structure
2. **Combine queries**: Mix and match WHERE clauses to create custom views
3. **Add to daily notes**: Embed queries in your daily notes for quick progress tracking
4. **Create dashboards**: Combine multiple queries in a single note for a complete overview
5. **Filter by date ranges**: Use `date(today) - dur(X days)` for time-based filtering
6. **Export data**: Use TABLE queries to export data for external analysis

## Example Dashboard Layout

Create a file called `problem-dashboard.md` with multiple queries:

```markdown
# Problem Solving Dashboard

## Today's Tasks
[Query 7: Problems Due for Review]

## Recent Activity
[Query 3: Recent Solved Problems]

## Progress Overview
[Query 16: Platform Summary Statistics]

## Focus Areas
[Query 30: Weak Topics]
```

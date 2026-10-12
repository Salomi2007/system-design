
jobs = {
    101: {"title": "Data Analyst", "company": "ABC Tech"},
    102: {"title": "Python Developer", "company": "XYZ Solutions"},
    103: {"title": "Web Developer", "company": "Tech India"}
}

applications = {}

while True:
    print("\n--- JOB RECRUITMENT PLATFORM ---")
    print("1. Search Jobs")
    print("2. View Job Details")
    print("3. Apply for Job")
    print("4. Check Application Status")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        keyword = input("Enter job title: ").lower()
        for job_id, job in jobs.items():
            if keyword in job["title"].lower():
                print(job_id, job["title"], "-", job["company"])

    elif choice == "2":
        job_id = int(input("Enter Job ID: "))
        if job_id in jobs:
            print(jobs[job_id])
        else:
            print("Job not found")

    elif choice == "3":
        user_id = input("Enter User ID: ")
        job_id = int(input("Enter Job ID: "))
        if job_id in jobs:
            applications[user_id] = {
                "job": jobs[job_id]["title"],
                "status": "Applied"
            }
            print("Application submitted successfully!")
        else:
            print("Job not found")

    elif choice == "4":
        user_id = input("Enter User ID: ")
        if user_id in applications:
            print("Job:", applications[user_id]["job"])
            print("Status:", applications[user_id]["status"])
        else:
            print("No application found")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")

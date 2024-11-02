<h1>Library Management System</h1>

<p>This is a Python-based Library Management System for the Brickfields Kuala Lumpur Community Library. It allows the management of the library's book catalogue, book loan records, and member information, as well as the account details of librarians and members. The data for this system is stored in text files for easy access and maintenance.</p>

<h2>Features</h2>

<h3>1. System Administrator</h3>
<ul>
    <li><strong>Account Management</strong>: Create and manage library member accounts. Add, view, search, edit, and remove librarian accounts.</li>
    <li><strong>Member Information Management</strong>: Add, view, search, edit, and remove member information.</li>
    <li><strong>Login and Logout</strong>: Secure login for system administrators.</li>
</ul>

<h3>2. Librarian</h3>
<ul>
    <li><strong>Book Catalogue Management</strong>: Add, view, search, edit, and remove books in the catalogue.</li>
    <li><strong>Book Loan Process</strong>: Manage book loans and check user eligibility (limit: 5 books, no overdue loans).</li>
    <li><strong>Login and Logout</strong>: Secure login for librarians.</li>
</ul>

<h3>3. Library Member</h3>
<ul>
    <li><strong>View Loaned Books</strong>: View currently loaned books, due dates, and calculate overdue fees based on the number of days overdue.</li>
    <li><strong>Search Book Catalogue</strong>: Search and view book availability.</li>
    <li><strong>Profile Management</strong>: Update profile information.</li>
    <li><strong>Login and Logout</strong>: Secure login for library members.</li>
</ul>

<h3>Overdue Fees (RM)</h3>
<table>
    <thead>
        <tr>
            <th>Days Overdue</th>
            <th>Fee (RM)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1 day</td>
            <td>2.00</td>
        </tr>
        <tr>
            <td>2 days</td>
            <td>3.00</td>
        </tr>
        <tr>
            <td>3 days</td>
            <td>4.00</td>
        </tr>
        <tr>
            <td>4 days</td>
            <td>5.00</td>
        </tr>
        <tr>
            <td>5 days</td>
            <td>6.00</td>
        </tr>
        <tr>
            <td>More than 5 days</td>
            <td>10.00</td>
        </tr>
    </tbody>
</table>

<h2>System Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>No additional libraries required (all functionality is built using Python's standard libraries).</li>
    <li>Data is stored in text files.</li>
</ul>

<h2>How to Run</h2>
<ol>
    <li>Clone this repository.</li>
    <li>Navigate to the project directory.</li>
    <li>Run <code>python Libraryproject.py</code> to start the application.</li>
</ol>

<h2>Data Storage</h2>
<ul>
    <li><strong>Text Files</strong>: User, librarian, and book data is stored and managed through text files. No external database is required.</li>
</ul>

<h2>Validation</h2>
<ul>
    <li>Input validation ensures correct and logical data entries.</li>
    <li>Users are notified of incorrect or invalid inputs during interaction with the system.</li>
</ul>

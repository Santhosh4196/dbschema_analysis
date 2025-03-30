#SP to drop and clean up schema
/****** Object:  StoredProcedure [dbo].[P_DROP_TEST_SCHEMA]    Script Date: 3/25/2025 2:38:37 PM ******/
'''SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE   PROCEDURE [dbo].[P_DROP_TEST_SCHEMA]
AS
BEGIN
    -- Task 1: Drop all tables, views, and procedures in the Test schema
    DECLARE @sql NVARCHAR(2000)

    -- Drop all tables in the Test schema
    SET @sql = ''
    SELECT @sql = @sql + 'DROP TABLE IF EXISTS [Test].[' + TABLE_NAME + ']; '
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_SCHEMA = 'Test' and TABLE_TYPE='BASE TABLE'

    EXEC sp_executesql @sql

    -- Drop all views in the Test schema
    SET @sql = ''
    SELECT @sql = @sql + 'DROP VIEW  [Test].[' + TABLE_NAME + ']; '
    FROM INFORMATION_SCHEMA.VIEWS 
    WHERE TABLE_SCHEMA = 'Test' 

    EXEC sp_executesql @sql

    -- Drop all procedures in the Test schema
    SET @sql = ''
    SELECT @sql = @sql + 'DROP PROCEDURE IF EXISTS [Test].[' + ROUTINE_NAME + ']; '
    FROM INFORMATION_SCHEMA.ROUTINES 
    WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_SCHEMA = 'Test'

    EXEC sp_executesql @sql

    -- Task 2: Drop the Test schema
    IF EXISTS (SELECT * FROM sys.schemas WHERE name = 'Test')
    BEGIN
        EXEC('DROP SCHEMA Test')
    END

	/*
    -- Task 3: Display a list of all tables in the dbo schema and get user input
	SQL query to get list of tables from UAT:
select CONCAT('''',TABLE_NAME,'''', ',') AS FormattedColumn from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='dbo' order by TABLE_NAME
    SELECT TABLE_NAME 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_SCHEMA = 'dbo'

    -- A placeholder for manual action by the user to remove specific dbo tables.
    PRINT 'Please note: Review the table list and manually drop desired tables as needed.'
	*/
END
GO

'''
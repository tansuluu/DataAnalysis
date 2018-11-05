FirstSecondMax(int
A[], int l, int r)
{
// Output
result
Result
res;
res.max1 = A[l];
res.max2 = A[l];

// if array has only one element
return null
record
if (l == r) return res;

// Base
case
when
array
has
only
two
elements
if (r - l == 1)
    {
    element
    // is the
    first
    maximum
    if (A[r] >= A[l])
    {
        res.max1 = A[r];
    res.max2 = A[l];
    }
    else
    {
        res.max1 = A[l];
    res.max2 = A[r];
    }

    return res;
    }

    // Find
    middle
    element
    int
    m = (l + r) / 2;

    // Find
    the
    largest
    two
    elements in each
    half
    Result
    lres = FirstSecondMax(A, l, m);
    Result
    rres = FirstSecondMax(A, m + 1, r);

    // So
    far
    we
    got
    4
    max
    values
    2
    on
    each
    half
    // so
    we
    need
    to
    merge
    them and take
    out
    only
    // two.Basically
    you
    compare
    the
    largest
    element
    // on
    the
    right
    side
    with the largest element on
    // the left side and take the greater one as the
    // result first max.In case the taken one was the
    // first max on the right then you need to compare
    // the second max on the right with the first max
    // on the left.If it is greater then you take it
    // as the second max otherwise you take the first
    // max on the left as the result second max.You
    // do the same if the taken one was on the left.
    // The code segment below demonstrates that

    // First max on the right is greater than
    // first max on the left
    if (rres.max1 >= lres.max1)
    {
    // Take
    the
    first
    max
    on
    the
    right
    res.max1 = rres.max1;

    // Compare
    second
    max
    on
    the
    right
    with
        // first
        max
        on
        the
        left
    if (rres.max2 >= lres.max1)
        {
            res.max2 = rres.max2;
        }
        else
        {
            res.max2 = lres.max1;
        }
        }
        // First
        max
        on
        the
        left is greater
        than
        // first
        max
        on
        the
        right
        else
        {
        // Take
        the
        first
        max
        on
        the
        left
        res.max1 = lres.max1;

        // Compare
        second
        max
        on
        the
        left
        with
            // first
            max
            on
            the
            right
        if (lres.max2 >= rres.max1)
            {
                res.max2 = lres.max2;
            }
            else
            {
                res.max2 = rres.max1;
            }
            }

            return res;
            }

            // Main
            function
            void
            main()
            {
            // Input
            array
            int
            A[] = {1, 5, 2, 4, 3};

            // Find
            first and second
            max
            elements
            Result
            res = FirstSecondMax(A, 0, 4);

            // Print
            output
            cout << res.max1 << " : " << res.max2 << endl;
            }